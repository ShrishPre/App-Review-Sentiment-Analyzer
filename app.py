
import streamlit as st
import joblib
import re

# Loading my model
model = joblib.load("sentiment.pkl")

# Text cleaning 
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

st.title("App Review Sentiment Analyzer")

st.write("Enter an app review below to predict whether it is Positive or Negative.")

user_input = st.text_area("Enter Review:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        cleaned = clean_text(user_input)
        prediction = model.predict([cleaned])[0]

        if prediction == 1:
            st.success("Sentiment: Positive 😊")
        else:
            st.error("Sentiment: Negative 😞")