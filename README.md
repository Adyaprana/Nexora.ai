<p align="center">
  <img src="assets\generated-icon.png" alt="Multimodal Chatbot Logo" width="120"/>
</p>

<h1 align="center">Nexora.ai</h1>

<p align="center">
  🌐 A smart, AI-powered assistant that understands <strong>text</strong>, <strong>voice</strong>, <strong>images</strong>, and <strong>PDFs</strong>.  
  <br />
  🤖 Built using Mistral LLM + Streamlit.
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/built%20with-streamlit-orange"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-green.svg"></a>
  <a href="https://linkedin.com/in/adyaprana21"><img src="https://img.shields.io/badge/connect-linkedin-blue"></a>
</p>

---

## 🖼️ Demo

> 🎬 *Check out a quick walkthrough of the app below:*

 <img src="assets\Home.png" width="600"/>

🔗 **Live Demo:**  
[Visit App on Render](https://nexora-ai-2wcg.onrender.com)  
[LinkedIn Post](https://www.linkedin.com/posts/adyaprana21_codecomplete-teamkiit-include-activity-7316729214173335552-V1v6)

---

## 🚀 Features

- ✅ **Multimodal Input** — Accepts **text**, **speech**, **images**, and **PDFs**
- 🧠 **Domain-Specific AI** — Tailored responses for **Education**, **Healthcare**, etc.
- 🖥️ **Responsive UI** — Sidebar navigation, loading animations, dark mode–ready
- ⚡ **Real-time Response** — Powered by **Mistral LLM API**

---

## 🛠️ Tech Stack

| Tool         | Role                      |
|--------------|---------------------------|
| Python       | Backend logic             |
| Streamlit    | UI & Web App Framework    |
| Mistral API  | LLM for response generation |
| SpeechRecognition | Voice input support |
| PyTesseract  | OCR from images           |
| PyPDF2       | PDF text extraction       |

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/multimodal-chatbot.git
cd multimodal-chatbot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add MISTRAL API key to `.streamlit/secrets.toml`
[mistral]
api_key = "YOUR_MISTRAL_API_KEY"

# 5. Run the application
streamlit run app.py
```
☁️ Deployment
You can easily deploy this app to any modern cloud platform:

🌐 Render

🚀 Streamlit Cloud

📦 Heroku

🔑 Note: Always store sensitive credentials (e.g., MISTRAL_API_KEY) securely using environment variables or the .streamlit/secrets.toml file.

🔮 Future Roadmap
Here's what's planned for future enhancements:

🧩 Plugin System — Add modular support for more domains (e.g., Finance, Law, etc.)

💬 Conversational Memory — Retain context across sessions and chats

🌍 Multilingual Support — Understand and respond in multiple languages

🔐 Robust Error Handling — Better validation, fallback messages, and user alerts

💡 Have a feature request? Feel free to open an issue or suggest enhancements!

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

👨‍💻 Author
Adyaprana Pradhan
