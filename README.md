# ⚡ APIForge

An AI-powered REST API generator that turns plain English descriptions 
into production-ready code. Describe what you want to build, pick your 
language and framework, and get a complete working API in seconds.

🔗 **Live Demo:** https://zippy-tiramisu-b7de12.netlify.app

---

## ✨ Features

- **AI Generation** — Describe your API in plain English and get complete working code
- **Multi-language** — Generate APIs in Python, JavaScript and Go
- **Multi-framework** — FastAPI, Flask, Django, Express, Fastify, Gin and Echo
- **Syntax Highlighting** — Beautiful code display with JetBrains Mono font
- **Route Visualization** — See all your API endpoints with color coded HTTP methods
- **Setup Instructions** — Step by step instructions to run your generated API
- **One Click Download** — Download your API as a ready to run file
- **Generation History** — Last 10 generated APIs saved locally in your browser
- **Example Prompts** — Quick start chips to inspire your first generation

---

## 🛠️ Built With

- [Python](https://python.org)
- [FastAPI](https://fastapi.tiangolo.com)
- [Groq API](https://console.groq.com) (LLaMA 3.3 70B)
- [Highlight.js](https://highlightjs.org) for syntax highlighting
- HTML, CSS, JavaScript (vanilla)
- Deployed on Render and Netlify

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/saipraneethp7/apiforge.git
cd apiforge
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

**4. Add your API key**

Create a `.env` file inside the `backend` folder:
GROQ_API_KEY=your_groq_key_here

Get a free Groq key at https://console.groq.com

**5. Run the backend**
```bash
uvicorn main:app --reload
```

**6. Open the frontend**

Open `frontend/index.html` with Live Server in VS Code.

---

## 📁 Project Structure
apiforge/
├── backend/
│   ├── main.py           # FastAPI routes and request handling
│   ├── generator.py      # AI generation logic and prompt engineering
│   ├── requirements.txt  # Python dependencies
│   └── .env              # API keys (not committed)
├── frontend/
│   ├── index.html        # Landing page
│   └── generator.html    # Main generator tool
├── .gitignore
└── README.md

---

## 💡 Example Prompts

- "A REST API for a blog with posts, comments and user authentication"
- "An e-commerce API with products, cart, orders and payments"
- "A task management API with projects, tasks, assignees and deadlines"
- "A social media API with users, posts, likes, follows and notifications"
- "A restaurant API with menu items, orders, tables and reservations"

---

## 👤 Author

**Sai Praneeth**
- GitHub: [@saipraneethp7](https://github.com/saipraneethp7)
- University: UMKC, CS Class of 2026

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).