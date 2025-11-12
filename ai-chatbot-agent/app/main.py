from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import subprocess
import json
import time

app = FastAPI()

# Serve static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def serve_home():
    return FileResponse("app/static/index.html")


@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return JSONResponse({"response": "Please type something 😊"})

        # Show thinking delay
        time.sleep(1.5)

        # 🧠 Generate a dynamic AI response using Ollama
        result = subprocess.run(
            ["ollama", "run", "llama3", user_message],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return JSONResponse({"response": "⚠️ Ollama error: " + result.stderr.strip()})

        # Extract model output
        model_reply = result.stdout.strip()

        # Optional trimming to remove unwanted console formatting
        model_reply = model_reply.split("\n")[-1]

        return JSONResponse({"response": model_reply})

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
