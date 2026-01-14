import os
import json
import time
from flask import Flask, redirect, url_for, session, render_template, request
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "super-secret-key")

# Gemini client (uses GEMINI_API_KEY automatically)
client = genai.Client()

# OAuth setup
oauth = OAuth(app)

google = oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    userinfo_endpoint="https://www.googleapis.com/oauth2/v2/userinfo",
    client_kwargs={
        "scope": "openid email profile"
    }
)

# ---------------------------
# Utility: Gemini retry logic
# ---------------------------

def generate_with_retry(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except ServerError:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise

# ---------------------------
# Routes
# ---------------------------

@app.route("/")
def home():
    if "user" not in session:
        return render_template("index.html")
    return redirect("/dashboard")


@app.route("/login")
def login():
    redirect_uri = url_for("https://gamidea.onrender.com/login/callback", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/login/callback")
def auth_callback():
    token = google.authorize_access_token()
    user_info = google.get("https://www.googleapis.com/oauth2/v2/userinfo").json()

    session["user"] = user_info
    return redirect("/dashboard")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    generated_prompt = None

    if request.method == "POST":
        idea = request.form.get("idea")
        prompt_type = request.form.get("prompt_type")
        genre = request.form.get("genre")
        style = request.form.get("style")
        platform = request.form.get("platform")

        # Structured JSON Prompt
        system_prompt = f"""
You are a AAA game designer.

Generate a game concept in JSON format using this structure:

{{
  "title": "",
  "genre": "",
  "platforms": "",
  "logline": "",
  "features": [],
  "setting": "",
  "lore": "",
  "protagonists": "",
  "antagonists": "",
  "gameplay_loop": "",
  "tone": "",
  "usp": ""
}}

Theme:
{idea}

Prompt Type: {prompt_type}
Genre: {genre}
Style: {style}
Platform: {platform}

Rules:
- Return ONLY valid JSON
- No markdown
- No explanation
"""

        try:
            raw_json = generate_with_retry(system_prompt)
            generated_prompt = json.loads(raw_json)

        except ServerError:
            # Fallback response if Gemini is overloaded
            generated_prompt = {
                "title": "⚠ AI Model Busy",
                "genre": "System Status",
                "platforms": "Cloud AI",
                "logline": "The AI model is currently overloaded. Please try again in a few seconds.",
                "features": [
                    "Automatic retry enabled",
                    "No data lost",
                    "System operational"
                ],
                "setting": "Google Gemini Cloud Infrastructure",
                "lore": "High traffic across the AI network caused a temporary delay.",
                "protagonists": "You, the developer",
                "antagonists": "Heavy server load",
                "gameplay_loop": "Click Generate again after a few seconds.",
                "tone": "Operational",
                "usp": "Enterprise-grade fault tolerance"
            }

        except json.JSONDecodeError:
            generated_prompt = {
                "title": "⚠ Formatting Error",
                "genre": "System Error",
                "platforms": "AI Output",
                "logline": "The AI returned invalid data format. Please try again.",
                "features": ["Auto recovery", "Safe rendering"],
                "setting": "AI Output Parser",
                "lore": "Unexpected response format received from model.",
                "protagonists": "Prompt Engine",
                "antagonists": "Malformed JSON",
                "gameplay_loop": "Regenerate prompt.",
                "tone": "Debug",
                "usp": "Self-healing AI system"
            }

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=generated_prompt
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------------------
# Run Server
# ---------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

