import requests
import base64
import json


import PyPDF2
import speech_recognition as sr
from PIL import Image
import io
import streamlit as st

# Load MistralAPI key from Streamlit secrets (ensure .streamlit/secrets.toml is set up)
MISTRAL_API_KEY = st.secrets["MISTRAL_API_KEY"]
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {MISTRAL_API_KEY}",
    "Content-Type": "application/json"
}

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# Function to convert speech to text
def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "Sorry, could not understand audio."
    except sr.RequestError:
        return "Could not request results, please check your internet."

# Function to convert image to base64 (for potential future image processing)
def encode_image(image_file):
    img_bytes = image_file.read()
    encoded = base64.b64encode(img_bytes).decode("utf-8")
    return encoded

# Main function: Handles different input modes and calls the Mistral API
def get_response(user_input, mode="text", file=None):
    prompt = ""

    # Choose prompt based on input mode
    if mode == "text":
        prompt = user_input
    elif mode == "voice":
        prompt = speech_to_text(file)
    elif mode == "pdf":
        prompt = extract_text_from_pdf(file)
    elif mode == "image":
        prompt = "User uploaded an image. Please describe its contents."  # Placeholder

    # Prepare payload with system prompt from selected domain if desired
    payload = {
        "model": "mistral-small",  # Adjust model if necessary
        "messages": [
            {"role": "system", "content": "You are a helpful multimodal assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(MISTRAL_API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            data = response.json()
            # Optional: Uncomment the next line to debug the full API response
            # st.write("DEBUG Response:", data)
            if 'choices' in data and len(data['choices']) > 0:
                reply = data['choices'][0]['message']['content']
                return reply
            else:
                return "❌ Error: Unexpected response format from Mistral API."
        else:
            return f"❌ API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
