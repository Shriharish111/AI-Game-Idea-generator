# ⚡ AI Prompt Generator Console

A cyberpunk-themed AI Prompt Generator powered by **Google Gemini AI** and **Google OAuth** authentication.

This web application allows users to sign in with Google and generate structured, studio-style game concepts using AI.  
The interface is designed like a futuristic game development console.

---

## 🚀 Features

- Google Sign-In (OAuth 2.0)
- Gemini AI integration (latest SDK)
- Structured game concept generation
- Cyberpunk neon UI
- Interactive design document cards
- Cyberpunk loading animation
- Mobile responsive design
- Automatic retry if AI model is busy
- Safe error handling

---

## 🧰 Tech Stack

| Layer       | Technology |
|------------|------------|
| Backend    | Python, Flask |
| AI Engine  | Google Gemini API |
| Auth       | Google OAuth (Authlib) |
| Frontend   | HTML, CSS (Cyberpunk UI) |
| Hosting    | Render |
| Versioning | Git + GitHub |

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

## 🔧 Local Installation

### 1. Clone Repository

bash
git clone https://github.com/yourusername/ai-prompt-generator.git
cd ai-prompt-generator

### 2. Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install Dependencies

bash
Copy code
pip install -r requirements.txt
### 4. Create Environment File
Create a file named .env

env
Copy code
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SECRET_KEY=any_random_string
###5. Run Application

bash
Copy code
python app.py
Open in browser:

cpp
Copy code
http://127.0.0.1:5000

---

## 🌍 Deployment on Render

Required Files
requirements.txt

start.sh

render.yaml

Environment Variables on Render
Add these in Render dashboard:

nginx
Copy code
GEMINI_API_KEY
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
SECRET_KEY
Google OAuth Redirect URL
Add in Google Cloud Console:

pgsql
Copy code
https://your-app-name.onrender.com/login/callback

---

## 🧠 How It Works

- User logs in using Google

- Enters a game concept idea

- Gemini AI generates structured JSON output

- Flask parses the JSON

- UI renders interactive cyberpunk cards

- Loading animation plays while AI generates

---

## 📄 Output Format

- Each generated concept includes:

- Game Title

- Genre & Platforms

- Core Concept (Logline)

- Key Features

- World Setting

- Lore & Narrative

- Protagonists

- Antagonists

- Gameplay Loop

- Tone & Atmosphere

- Unique Selling Point

---

## 🎯 Use Cases

- Game concept ideation

- Story development

- World building

- Pitch document generation

- AI SaaS prototype

- Portfolio project

---

## 🔮 Planned Enhancements

- Save projects per user

- PDF export

- Shareable links

- Mobile PWA

- Prompt templates

- Admin dashboard

---

## 📜 License 

- - MIT License — Free to use and modify.

---

## 👨‍💻 Author 

- Shri Harish
- - Game Developer & AI Engineer
