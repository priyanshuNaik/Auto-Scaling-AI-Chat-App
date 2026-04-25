from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx, os

app = FastAPI(title='AI Chat API', version='1.0.0')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_URL = 'https://api.groq.com/openai/v1/chat/completions'

class PromptRequest(BaseModel):
    message: str

@app.get('/health')
def health(): return {'status': 'ok'}

@app.post('/chat')
async def chat(request: PromptRequest):
    headers = {'Authorization': f'Bearer {GROQ_API_KEY}'}
    payload = {
        'model': 'llama3-8b-8192',
        'messages': [{'role': 'user', 'content': request.message}]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_URL, json=payload, headers=headers)
    return response.json()
