import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AI Phishing Detector",
    page_icon="🛡️"
)

model = joblib.load("phishing_model.pkl")

if isinstance(model, dict):
    if "model" in model:
        model = model["model"]

st.title("🛡️ AI-Based Phishing Detection")
st.write("Enter a URL to analyze its phishing risk.")

url = st.text_input("Enter URL")

if st.button("Analyze URL"):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        try:
            url = url.lower()

            features = [
                len(url),
                url.count("."),
                url.count("/"),
                url.count("@"),
                url.count("?"),
                url.count("-"),
                url.count("_"),
                url.count("%"),
                url.count("&"),
                url.count("="),
                url.count(":"),
                url.count("~"),
                url.count("www"),
                url.count("http"),
                url.count("https"),
                int(url.startswith("https")),
                int(url.startswith("http")),
                len(url.split(".")),
                len(url.split("/")),
                url.count("#"),
                url.count("$"),
                url.count("'"),
                url.count('"'),
                url.count(" ")
            ]

            dataset = pd.DataFrame([features])

            prediction = model.predict(dataset)[0]
            probability = model.predict_proba(dataset)[0]

            if prediction == 1:
                st.error("🚨 Phishing URL detected!")
            else:
                st.success("✅ Safe URL")

            st.write(
                f"Confidence: {max(probability) * 100:.2f}%"
            )

        except Exception as e:
            st.error(f"Error: {e}")