import streamlit as st
import requests
import json
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, "r") as file:
        return json.load(file)

def initialize_chat_history():
    """Initialize the chat history in session state if it doesn't exist."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "test_mode" not in st.session_state:
        st.session_state.test_mode = False  # Full mode unless token is missing

def clear_chat_history():
    """Clear the chat history from session state."""
    st.session_state.messages = []

def get_chatbot_response(prompt, model="mistral-medium"):
    """
    Get a chatbot response using Mistral AI API.
    """
    # Retrieve API key from secrets (either top-level or under [mistral])
    api_key = st.secrets.get("api_token")
    if not api_key and "mistral" in st.secrets:
        api_key = st.secrets["mistral"].get("api_token")
    
    if not api_key:
        st.warning("⚠️ Mistral API token not found. Running in test mode.")
        st.session_state.test_mode = True
        return "This is a test response. The chatbot is running in test mode."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 500
    }

    API_URL = "https://api.mistral.ai/v1/chat/completions"

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        st.error(f"Error: {response.text}")
        return None

    result = response.json()
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    return "Error: Invalid response"

def display_chat_message(role, content, domain_config):
    """Display a chat message with appropriate styling."""
    if role == "user":
        st.markdown(f'<div class="user-message">{content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message">{content}</div>', unsafe_allow_html=True)

def format_chat_for_export(messages, domain):
    """Format chat history for export."""
    export_data = {
        "domain": domain,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "conversation": []
    }
    for msg in messages:
        export_data["conversation"].append({
            "role": msg["role"],
            "content": msg["content"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return json.dumps(export_data, indent=2)
