from fastapi import FastAPI, Request
import joblib
import pandas as pd

app = FastAPI()

# Load model trained with train_model.py
model = joblib.load("model.joblib")

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}
