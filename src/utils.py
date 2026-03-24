import re
import pandas as pd


def clean_password(password):
    if pd.isna(password):
        return ""
    return str(password).strip()


def load_data(file_path):
    df = pd.read_csv(file_path)

    if "password" not in df.columns or "strength" not in df.columns:
        raise ValueError("Dataset must contain 'password' and 'strength' columns.")

    df["password"] = df["password"].apply(clean_password)
    df = df[df["password"] != ""]
    return df


def validate_password_input(password):
    if not password or not isinstance(password, str):
        return False, "Please enter a valid password."
    if len(password.strip()) == 0:
        return False, "Password cannot be empty."
    return True, ""


def generate_password_feedback(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Use at least 8 characters.")
    if not re.search(r"[a-z]", password):
        feedback.append("Add at least one lowercase letter.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Add at least one uppercase letter.")
    if not re.search(r"\d", password):
        feedback.append("Include at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\];'`~]", password):
        feedback.append("Include at least one special character.")

    common_passwords = {
        "password", "123456", "123456789", "qwerty", "admin",
        "password123", "welcome", "abc123"
    }

    if password.lower() in common_passwords:
        feedback.append("Avoid using very common passwords.")

    if len(set(password)) < 4:
        feedback.append("Use more unique characters.")

    return feedback
