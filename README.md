# Odia AI Translator

An AI-powered web application that translates Odia text into multiple languages including:

- English
- Hindi
- Spanish
- Mandarin Chinese

The application provides a simple and user-friendly interface for translating Odia text and can be extended with speech-to-text and text-to-speech capabilities.

---

## Features

✅ Odia to English Translation

✅ Odia to Hindi Translation

✅ Odia to Spanish Translation

✅ Odia to Mandarin Chinese Translation

✅ Responsive Web Interface

✅ Copy Translation Output

✅ Dark Mode Support

✅ Fast API Backend

✅ AI Translation Integration

---

## Technology Stack

### Frontend
- React
- TypeScript
- Tailwind CSS
- Lovable

### Backend
- Python
- FastAPI

### Translation Engine
- Google Translate API
- Meta NLLB-200 (Optional)
- IndicTrans2 (Optional)

---

## Project Structure

```text
odia-ai-translator/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── models/
│
├── README.md
└── LICENSE
git clone https://github.com/yourusername/odia-ai-translator.git

cd odia-ai-translator
pip install fastapi uvicorn googletrans==4.0.0rc1
uvicorn main:app --reload
Server will start at:

http://localhost:8000
API Endpoint
Translate Text

POST

/translate

Request:

{
  "text": "ମୋର ନାମ ଅଶ୍ୱିନୀ",
  "target_language": "en"
}

Response:

{
  "translated_text": "My name is Aswini"
}
Supported Languages
Language	Code
Odia	or
English	en
Hindi	hi
Spanish	es
Mandarin Chinese	zh-cn
Future Enhancements
Odia Speech-to-Text
Text-to-Speech Output
Translation History
User Authentication
Mobile Application
Offline Translation
AI-powered Translation Models
Multi-language Speech Translation
Deployment
Frontend
Vercel
Netlify
Backend
Railway
Render
AWS
Azure
Use Cases
Language Learning
Education
Government Services
Tourism
Business Communication
Multilingual Accessibility
Contributing

Contributions are welcome.

Fork the repository
Create a feature branch
Commit changes
Push changes
Create a Pull Request
License

This project is licensed under the MIT License.

Author

Aswini Kumar Biswal

AI/ML Engineer | Speech AI Enthusiast

Focused on multilingual AI systems, speech technologies, and Odia language processing.


This README gives contributors and users a clear overview of the project's purpose, setup instructions, API usage, features, and future roadmap.
