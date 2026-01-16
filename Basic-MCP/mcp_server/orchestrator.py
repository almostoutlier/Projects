from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# Set URL for FastAPI local model (inside Docker, service name)
LOCAL_MODEL_URL = os.getenv("LOCAL_MODEL_URL", "http://fastapi_app:8000/predict")

@app.get("/")
def home():
    return {"message": "MCP server routing to local model only"}

@app.post("/infer")
async def infer(request: Request):
    data = await request.json()
    try:
        response = requests.post(LOCAL_MODEL_URL, json=data)
        return {"source": "local_model", "response": response.json()}
    except Exception as e:
        return {"error": str(e)}
