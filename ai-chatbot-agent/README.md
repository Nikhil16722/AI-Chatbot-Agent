# 🤖 AI Chatbot Agent — Powered by FastAPI & Ollama

![Chatbot Preview](app/static/niki0.png)

## 🌟 Overview

**AI Chatbot Agent** is a smart, interactive chatbot built with **FastAPI**, **HTML**, **CSS**, and **JavaScript** that connects to a **local Ollama LLM** (Large Language Model) to generate natural language responses — fully offline.

It features:

* 🧠 Real AI-generated responses (no hardcoded replies)
* ⚡ FastAPI backend for smooth async processing
* 🎨 Beautiful UI with animated glass effect
* 🌅 Fixed aesthetic background image
* 💬 “Thinking…” typing simulation
* 🖥️ Completely offline (works with Ollama locally)

---

## 🚀 Tech Stack

| Layer         | Technology Used                          | Purpose                                        |
| ------------- | ---------------------------------------- | ---------------------------------------------- |
| **Backend**   | [FastAPI](https://fastapi.tiangolo.com/) | Handles API routes for chat messages           |
| **Frontend**  | HTML, CSS, JavaScript                    | Interactive chat interface                     |
| **AI Engine** | [Ollama](https://ollama.ai)              | Runs local LLMs (like Llama 3, Phi-3, Mistral) |
| **Runtime**   | Python 3.10+                             | Application base                               |
| **Server**    | [Uvicorn](https://www.uvicorn.org/)      | ASGI server for running FastAPI                |

---

## 🧩 Project Structure

```
ai-chatbot-agent/
│
├── app/
│   ├── main.py               # FastAPI backend logic
│   ├── chat.py               # (Optional) Chat utilities
│   ├── ingest.py             # (Optional) Knowledge ingestion
│   ├── retrieval.py          # (Optional) Vector search
│   ├── utils.py              # Helper functions
│   ├── static/
│   │   ├── index.html        # Chat UI
│   │   ├── style.css         # Front-end styling
│   │   ├── script.js         # Client-side logic
│   │   └── niki.jpg          # Background image
│   └── __init__.py
│
├── data/                     # Sample text / knowledge data
│   ├── ai_intro.txt
│   ├── company_info.txt
│   └── notes.md
│
├── requirements.txt          # Required Python packages
├── Dockerfile                # (Optional) For containerization
├── .env                      # Environment config
├── README.md                 # Documentation
└── run.sh                    # Script to launch app
```

---

## ⚙️ Installation & Setup

### 🧱 Prerequisites

* Python 3.10 or above
* [Ollama](https://ollama.ai) installed and running locally
* Any modern browser

---

### 🧩 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-chatbot-agent.git
cd ai-chatbot-agent
```

---

### 🧩 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux
```

---

### 🧩 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🧩 4️⃣ Check Ollama

Run these commands to verify Ollama is active:

```bash
ollama list
ollama serve
```

✅ You should see:
`Listening on 127.0.0.1:11434`

Download a model (if not already):

```bash
ollama pull llama3
```

Test it:

```bash
ollama run llama3 "Hello!"
```

---

### 🧩 5️⃣ Run the Chatbot

```bash
uvicorn app.main:app --reload
```

Now visit 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 💬 How It Works

1. The user types a message in the chatbox.
2. The message is sent to FastAPI via `/chat` endpoint.
3. FastAPI calls Ollama locally (`ollama run llama3 "message"`).
4. Ollama generates a **real AI response**.
5. The frontend shows a typing animation ("🤖 Thinking...") before displaying the reply.
6. The conversation updates dynamically with a clean UI.

---

## 🖼️ UI Features

* 🌅 Background image (fixed, full screen)
* 💠 Glassmorphism chat window
* ✨ Smooth hover and shadow transitions
* 💬 Real-time message display
* ⏳ Typing/Thinking effect

---

## 📦 requirements.txt

```txt
fastapi
uvicorn
requests
pydantic
python-dotenv
```

---

## 🧠 Example Models to Use with Ollama

You can use any of these models:

| Model   | Command               | Size   | Description                     |
| ------- | --------------------- | ------ | ------------------------------- |
| Llama 3 | `ollama pull llama3`  | ~4.7GB | Great general-purpose model     |
| Phi 3   | `ollama pull phi3`    | ~2.5GB | Lightweight, fast for small PCs |
| Mistral | `ollama pull mistral` | ~4.1GB | Good for reasoning and Q&A      |
| Gemma   | `ollama pull gemma`   | ~3GB   | Smaller, conversational tone    |

To switch models, just edit `main.py` here:

```python
["ollama", "run", "llama3", user_message]
```

→ replace `"llama3"` with `"phi3"`, `"mistral"`, etc.

---

## 🧑‍💻 Example Interaction

**User:**

> What is Python?

**Bot:**

> Python 🐍 is a versatile, beginner-friendly programming language used in AI, data analytics, and automation.

**User:**

> Tell me about SQL

**Bot:**

> SQL 💾 helps you manage and query data efficiently in relational databases.

---

## 🧠 Future Enhancements

* 🧩 Add memory (context retention)
* 📚 Connect to your own documents or knowledge base
* 🗣️ Add speech-to-text and voice replies
* 🌐 Deploy online using Render / Vercel / Railway
* 💾 Integrate database logging for chat history

---

## 🧑‍💻 Author

**👤 Nikhil Lingala**
💻 *AI | Data Analytics | Automation Enthusiast*
📫 [LinkedIn](https://www.linkedin.com/in/nikhil-lingala-a26030266/) |

---

## 🪶 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

### 💡 Pro Tip

> If you want Ollama to start automatically every time you launch your chatbot:
>
> ```bash
> ollama serve --detach
> ```
>
> That keeps it running silently in the background 🚀

---
