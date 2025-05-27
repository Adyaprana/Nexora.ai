import streamlit as st
from main import get_response
from domain_prompts import DOMAIN_CONFIGS
from speech import recognize_speech


# Initialize session state variables
if 'domain' not in st.session_state:
    st.session_state.domain = None
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Set page configuration
st.set_page_config(page_title="Nexora.ai", page_icon="🤖", layout="wide")


st.markdown("""
<style>
/* Global Styling */
body {
  background-color: #f9f9f9;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #000;  /* Black text */
  margin: 0;
  padding: 0;
}

/* Header Styling */
.header-container {
  text-align: center;
  padding: 20px;
  background: #rgb(23, 45, 67);
  box-shadow: 0 2px 4px rgb(23, 45, 67);
  margin-bottom: 20px;
}
.header-container img {
  width: 100px;
}
.header-container h1 {
  font-size: 2.5rem;
  margin: 0;
  color: #white;
  background-color: rgb(23, 45, 67);
  padding: 5px;
  border-radius: 5px;
}

/* Sidebar Styling */
.sidebar {
  background-color: #ffffff;
  padding: 20px;
  border-right: 1px solid #ddd;
  height: 100vh;
  overflow-y: auto;
  color: #000;
}

/* Domain Container Styling */
.domain-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-bottom: 20px;
}

/* Domain Card Styling */
.domain-card {
  flex: 0 0 calc(50% - 16px);
  margin: 8px;
  background-color: rgb(23, 45, 67);
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s ease;
  text-align: center;
  color: #ffff;
}
.domain-card:hover {
  transform: scale(1.02);
}
.domain-card h3 {
  margin-top: 0;
  color: #fff;
}

/* Special Heading Styling */
h2 {
  color: #ff6600;  /* For "Choose Your Assistant Domain" */
  text-align: center;
  font-weight: bold;
  margin-bottom: 20px;
}

/* Chat Container */
.chat-container {
  background-color: #ffffff;
  border-radius: 8px;
  padding: 16px;
  margin: 8px 0;
  height: 500px;
  overflow-y: auto;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  color: #000;
}

/* Messages */
.message {
  padding: 10px;
  border-radius: 8px;
  margin: 10px 0;
}
.message.user {
  background-color: rgb(136, 69, 182);
  color: white;
  text-align: right;
}
.message.assistant {
  background-color: rgb(23, 45, 67);
    color: white;
  text-align: left;
}

/* Input Area */
.input-area {
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Footer Styling */
.footer {
  text-align: center;
  padding: 15px;
  background-color: rgb(23, 45, 67);
  color: #888;
  font-size: 0.9rem;
  margin-top: 20px;
  border-top: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)


# Header with logo and title
st.markdown("""
<div class="header-container">
    <h1>🤖 Nexora.ai</h1>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("assets/generated-icon.png", width=280)

    st.title("Navigation")
    nav_option = st.radio("Go to", ["Chat", "About Project", "Technology", "Future Scope"], key="nav_radio")


# Session Initialization
if 'domain' not in st.session_state:
    st.session_state.domain = None
if 'messages' not in st.session_state:
    st.session_state.messages = []

# ---------------- Navigation Handling ---------------- #
if nav_option != "Chat":
    if nav_option == "About Project":
        st.markdown("""
            ## About Project
            This project is a Multimodal Virtual Assistant designed to process inputs via text, voice, image, and PDF.
            It leverages AI/LLM (using the Mistral API) to generate intelligent, context-aware responses across various domains.
        """)
    elif nav_option == "Technology":
        st.markdown("""
            ## Technology Used
            - **Programming Language:** Python
            - **Framework:** Streamlit
            - **Libraries:** pytesseract (OCR), SpeechRecognition, PyPDF2, PyMuPDF, Pillow
            - **APIs:** Mistral AI API for chatbot responses
            - **Deployment:** Streamlit Cloud / Render / Vercel
        """)
    elif nav_option == "Future Scope":
        st.markdown("""
            ## Future Scope / Limitations
            - Enhance image captioning and real-time voice synthesis.
            - Integrate multilingual support and more advanced AI models.
            - Improve cloud scalability and deploy on public cloud platforms.
            - Address limitations in response latency and UI responsiveness.
        """)

# ---------------- Chat Interface Section ---------------- #
else:
    if st.session_state.domain is None:
        st.subheader("Choose Your Assistant Domain")

        domains = list(DOMAIN_CONFIGS.keys())
        for i in range(0, len(domains), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(domains):
                    domain = domains[i + j]
                    with cols[j]:
                        st.markdown(f"""
                        <div class='domain-card'>
                            <h3>{DOMAIN_CONFIGS[domain]['icon']} {domain}</h3>
                            <p>{DOMAIN_CONFIGS[domain]['description']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button("Chat Now", key=f"chat_{domain}"):
                            st.session_state.domain = domain
                            st.session_state.messages = []
                            st.rerun()

    else:
        # Display Domain Info
        st.markdown(f"### {DOMAIN_CONFIGS[st.session_state.domain]['icon']} {st.session_state.domain}")
        st.write(DOMAIN_CONFIGS[st.session_state.domain]['description'])

        st.markdown("<hr>", unsafe_allow_html=True)

        # Display Chat History
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.messages:
                if msg['role'] == "user":
                    st.markdown(f"<div class='message user'><strong>You:</strong> {msg['content']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='message assistant'><strong>Assistant:</strong> {msg['content']}</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # Select Input Mode
        input_mode = st.radio("Select Input Mode:", ["Text", "Voice", "Image", "PDF"], key="input_mode_radio")

        user_query = ""

        if input_mode == "Text":
            user_query = st.text_input("Enter your query:", key="text_input")

        elif input_mode == "Voice":
            if st.button("🎤 Speak Now", key="record_button"):
                with st.spinner("Listening..."):
                   user_query = recognize_speech()  # Process voice input
            if user_query and "Could not process" not in user_query:
                st.success(f"Recognized: {user_query}")
                response = get_response(user_query)
                st.write(f"Response: {response}")
            else:
               st.error("❌ Could not process voice input. Please try again or check your mic.")


        elif input_mode == "Image":
            uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"], key="image_uploader")
            if uploaded_image:
                from image_processing import extract_text_from_image
                user_query = extract_text_from_image(uploaded_image)
                st.info(f"Extracted Text: {user_query}")

        elif input_mode == "PDF":
            uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"], key="pdf_uploader")
            if uploaded_pdf:
                from pdf_processing import extract_text_from_pdf
                user_query = extract_text_from_pdf(uploaded_pdf)
                st.info(f"Extracted Text: {user_query}")

# Send Query Button
        if st.button("Send Query", key="send_query"):
            if user_query.strip() != "":
                st.session_state.messages.append({"role": "user", "content": user_query})
        with st.spinner("Assistant is typing..."):
            response = get_response(user_query)
        st.session_state.messages.append({"role": "assistant", "content": response})

        if input_mode == "Voice":
            speak_text(response)  # Speak only if input was Voice



        if st.button("Change Domain", key="change_domain"):
            st.session_state.domain = None
        from io import StringIO
        chat_text = ""
        for msg in st.session_state.messages:
            role = "You" if msg["role"] == "user" else "Assistant"
            chat_text += f"{role}: {msg['content']}\n\n"

        st.download_button(
        label="Download Chat History",
        data=chat_text,
        file_name="nexora_chat.txt",
        mime="text/plain",
        key="download_button"
     )


# ---------------- Footer ---------------- #
st.markdown("""
<div class="footer">
    <p>Made with ❤️ by Adyaprana Pradhan | © 2025 All Rights Reserved</p>
    <p>Multimodal Virtual Assistant Chatbot | 🤖 Nexora.ai</p>
</div>
""", unsafe_allow_html=True)
