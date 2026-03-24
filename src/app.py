import streamlit as st
from src.predict import predict_password_strength
from src.utils import validate_password_input, generate_password_feedback

st.set_page_config(page_title="Password Strength Predictor", page_icon="🔐")

st.title("🔐 Password Strength Predictor")
st.write("Predict password strength using **TF-IDF + Logistic Regression**")

password = st.text_input("Enter a password", type="password")

if st.button("Check Strength"):
    is_valid, error_message = validate_password_input(password)

    if not is_valid:
        st.error(error_message)
    else:
        try:
            prediction, confidence = predict_password_strength(password)

            st.subheader("Prediction Result")

            if prediction.lower() == "weak":
                st.error(f"Strength: {prediction}")
            elif prediction.lower() == "medium":
                st.warning(f"Strength: {prediction}")
            else:
                st.success(f"Strength: {prediction}")

            if confidence is not None:
                st.write(f"**Confidence Score:** {confidence:.2%}")

            feedback = generate_password_feedback(password)

            st.subheader("Suggestions")
            if feedback:
                for item in feedback:
                    st.write(f"- {item}")
            else:
                st.success("Great password! No major improvements needed.")

        except FileNotFoundError as e:
            st.error(str(e))
