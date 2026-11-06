import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)


# Get project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load trained model
model = joblib.load(
    BASE_DIR / "models" / "spam_classifier.pkl"
)

# Load preprocessor
preprocessor = joblib.load(
    BASE_DIR / "models" / "preprocessor.pkl"
)

st.title("📧 Spam Email Detector")

st.write(
    "Enter your email message below "
    "to check whether it is Spam or Ham."
)

# Email Input
user_message = st.text_area(
    "Enter your email message:",
    placeholder="Type or paste your email here..."
)

predict_button = st.button(
    "Predict",
    use_container_width=True,
    type="primary"
)

if predict_button:
    if not user_message.strip():
        st.warning("Please enter an email message.")

    else:
        input_data = pd.DataFrame({
            "Message": [user_message.lower()],
            "Message_length": [len(user_message)]
        })
        input_features = preprocessor.transform(input_data)
        prediction = model.predict(input_features)[0]

        if prediction.lower() == "spam":
            st.error("🚨 This email is SPAM!")

        else:
            st.success("✅ This email is HAM (Not Spam).")

st.divider()

st.caption(
    "Spam Email Detector | "
    "Powered by Machine Learning"
)

st.caption(
    "Developed by Kenzy"
)
