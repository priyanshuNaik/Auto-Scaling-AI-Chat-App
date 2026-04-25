from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class Prompt(BaseModel):
    message: str

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.post("/chat")
def chat(prompt: Prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt.message}]
    }

    response = requests.post(url, json=data, headers=headers)
    print("STATUS:", response.status_code)  # 👈 debug
    print("RESPONSE:", response.text)       # 👈 debug
    return response.json()
