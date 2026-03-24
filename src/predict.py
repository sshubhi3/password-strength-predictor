import os
import joblib

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "logistic_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")


def load_model_and_vectorizer():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError(
            "Model files not found. Please run 'python -m src.train' first."
        )

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer


def predict_password_strength(password):
    model, vectorizer = load_model_and_vectorizer()
    password_tfidf = vectorizer.transform([password])

    prediction = model.predict(password_tfidf)[0]

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(password_tfidf)[0]
        confidence = max(probabilities)
    else:
        confidence = None

    return prediction, confidence
