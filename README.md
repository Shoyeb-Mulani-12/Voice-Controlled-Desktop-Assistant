# 🎙️ Voice Controlled Desktop Assistant

An intelligent Python-based desktop assistant that lets you control your computer using voice commands — with a bonus **Streamlit web version** for cloud deployment and demonstration.

---

## 📌 Overview

The Voice Controlled Desktop Assistant automates routine desktop tasks through natural voice interaction. It combines speech recognition, text-to-speech, and system automation into a seamless experience. The project ships in **two versions**:

| Version | Interface | Deployment |
|---|---|---|
| 🖥️ Desktop | Microphone + Voice | Local System |
| 🌐 Web (Streamlit) | Buttons + Text | Cloud / Browser |

---

## 🚀 Features

### 🖥️ Desktop Version
- 🎤 Voice command recognition
- 📝 Open Notepad and Calculator
- 🔋 Check battery status
- 🕐 Tell current time and date
- 🎵 Play music
- 🔍 Search Google
- ▶️ Open YouTube
- 🔒 Lock system
- ⚡ Shutdown and restart system

### 🌐 Web Version (Streamlit)
- 🕐 Show Indian Standard Time (IST)
- 📅 Display current date
- 🌍 Open websites (Google, YouTube, etc.)
- 📊 Show system health — CPU & RAM usage
- 🎛️ Interactive button-based UI

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Voice Input | `speech_recognition` |
| Text-to-Speech | `pyttsx3` |
| System Monitoring | `psutil` |
| Automation | `pyautogui` |
| Date & Time | `datetime`, `pytz` |
| Web Browsing | `webbrowser` |
| Web Framework | `Streamlit` |

---

## 📁 Project Structure

```
voice-controlled-assistant/
│
├── desktop_assistant.py      # Full desktop version with voice control
├── web_app.py                # Streamlit web version
├── requirements.txt          # Python dependencies
└── README.md
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Shoyeb-Mulani-12/voice-controlled-assistant.git
cd voice-controlled-assistant

# Install dependencies
pip install -r requirements.txt
```

### requirements.txt
```
speechrecognition
pyttsx3
psutil
pyautogui
pytz
streamlit
```

---

## ▶️ Usage

### Desktop Version
```bash
python desktop_assistant.py
```
> Ensure your microphone is connected and working.

### Web Version (Streamlit)
```bash
streamlit run web_app.py
```

---

## 🔄 How It Works

```
User gives command (voice / text)
        ↓
System processes the input
        ↓
Command matched with predefined actions
        ↓
Action executed
        ↓
Result displayed / spoken
```

---

## ⚠️ Limitations

- **Desktop version**: Requires a microphone; Windows-specific OS commands
- **Web version**: No microphone access; cannot control system operations due to cloud restrictions

---

## 🔮 Future Scope

- [ ] AI chatbot integration for natural language understanding
- [ ] Voice input support in the web version
- [ ] Mobile application development
- [ ] Smart home device integration
- [ ] Improved NLP for complex command parsing

---

## 👨‍💻 Developer

**Shoyeb Hamid Mulani**
- 📧 shoyebmulani4521@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/shoyeb-mulani)
- 💻 [GitHub](https://github.com/Shoyeb-Mulani-12)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
