# 🔐 Password Strength Predictor

A machine learning project that predicts whether a password is **Weak**, **Medium**, or **Strong** using **TF-IDF vectorization** and **Logistic Regression**.

## 🚀 Features
- Predicts password strength from user input
- Uses character-level TF-IDF for password text representation
- Trained using Logistic Regression
- Displays confidence score
- Provides rule-based suggestions to improve password quality
- Built with a Streamlit web interface

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit

## 📂 Project Structure
```bash
password-strength-predictor/
│
├── data/
│   └── passwords.csv
├── models/
├── src/
│   ├── __init__.py
│   ├── utils.py
│   ├── train.py
│   └── predict.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📊 Model Details
- Vectorizer: `TfidfVectorizer(analyzer='char', ngram_range=(1,3))`
- Model: `LogisticRegression(max_iter=1000)`
- Accuracy: **81.98%** (based on project dataset)

## ▶️ How to Run
```bash
pip install -r requirements.txt
python -m src.train
streamlit run app.py
```

## 📌 Example
Input: `P@ssw0rd123`  
Output: `Strong`

## 👩‍💻 Author
Your Name
