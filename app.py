import subprocess
import sys

# Function to install dependencies from requirements.txt
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")

# Call the function
install_requirements()

import streamlit as st
from transformers import pipeline
from deep_translator import GoogleTranslator
from langdetect import detect

# Initialize summarization pipeline with PyTorch (default in Hugging Face Transformers)
summarizer = pipeline("summarization", framework="pt")  # Use PyTorch (pt) explicitly

# Function to summarize the article
def summarize_article(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to detect the language and translate if necessary
def translate_text(text, target_language="en"):
    source_language = detect(text)
    if source_language != target_language:
        translator = GoogleTranslator(source=source_language, target=target_language)
        translated_text = translator.translate(text)
        return translated_text, source_language
    return text, source_language

# Streamlit UI
st.title("News Article Summarizer and Translator")

st.write("Enter the full news article in any language, and the app will summarize and translate it into English.")

# Input for article text
article_title = st.text_input("Enter the title of the article:")
article_content = st.text_area("Enter the article content:")

# Check if content is entered
if st.button("Summarize & Translate"):
    if article_content:
        # Detect language and translate
        translated_content, detected_language = translate_text(article_content)
        translated_title, _ = translate_text(article_title)
        
        # Summarize the translated article
        summary = summarize_article(translated_content)
        
        # Display results
        st.subheader("Original Language Detected:")
        st.write(detected_language)
        
        st.subheader("Translated Title:")
        st.write(translated_title)
        
        st.subheader("Translated Content:")
        st.write(translated_content)
        
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.error("Please enter the article content.")
