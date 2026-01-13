# ⚡ AI Prompt Generator Console

A futuristic cyberpunk-themed AI Prompt Generator powered by **Google Gemini AI** and **Google OAuth** authentication.  
This web app allows users to sign in with Google and generate structured, studio-style game concepts using AI.

Built with Flask and designed like a AAA game development console.

---

## 🚀 Features

- 🔐 Google Sign-In (OAuth 2.0)
- 🤖 Gemini AI integration (latest SDK)
- 🎮 Game concept prompt generator
- 🧠 Structured AI output (JSON → interactive UI)
- ⚡ Cyberpunk neon UI
- 🌀 Cyberpunk loading animation
- 📱 Mobile responsive
- 🔁 Automatic retry if AI model is busy
- 🛡 Safe error handling

---

## 🧰 Tech Stack

- **Backend:** Python, Flask  
- **AI:** Google Gemini API  
- **Auth:** Google OAuth (Authlib)  
- **Frontend:** HTML, CSS (Cyberpunk theme)  
- **Hosting:** Render  
- **Version Control:** Git + GitHub  

---

## 📸 UI Preview

Futuristic AI Console with:
- Neon glow panels
- Interactive cards
- Structured pitch documents
- Cyberpunk loading screen

---

## 📂 Project Structure

ai-prompt-generator/
├── app.py
├── requirements.txt
├── start.sh
├── render.yaml
├── .gitignore
├── templates/
│ ├── index.html
│ └── dashboard.html
├── static/
│ └── style.css
└── README.md

yaml
Copy code

---

## 🔧 Installation (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-prompt-generator.git
cd ai-prompt-generator
2. Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Create .env File
env
Copy code
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SECRET_KEY=any_random_string
5. Run App
bash
Copy code
python app.py
Open in browser:

cpp
Copy code
http://127.0.0.1:5000
🌍 Deployment (Render)
This project is production-ready and can be deployed on Render.

Required Files
start.sh

render.yaml

requirements.txt

Environment Variables on Render
nginx
Copy code
GEMINI_API_KEY
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
SECRET_KEY
Google OAuth Redirect URL
Add this in Google Cloud Console:

pgsql
Copy code
https://your-app-name.onrender.com/login/callback
🎯 How It Works
User logs in using Google

Enters a game idea

Gemini AI generates a structured game concept (JSON)

Flask parses JSON

UI renders it as interactive cyberpunk cards

Loading animation plays while AI generates

🧠 Example Output
Game Title

Genre & Platforms

Core Concept

Features

Setting & Lore

Protagonists

Antagonists

Gameplay Loop

Tone & Atmosphere

Unique Selling Point

All rendered in a futuristic AI console UI.

🏆 Use Cases
Game design ideation

Story development

World building

Creative pitching

Portfolio projects

AI SaaS prototype

🔮 Future Upgrades
Save projects per user

PDF export

Shareable links

Mobile PWA

Prompt templates

Admin dashboard

📜 License
MIT License — free to use and modify.

👨‍💻 Author
Built by Shri Harish
Game Developer & AI Engineer

⚡ "Design the future of games with AI."
