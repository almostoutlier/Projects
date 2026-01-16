FROM python:3.11-slim

WORKDIR /app

COPY ../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../fastapi_app /app

# Only train model if it's the FastAPI app
RUN test -f train_model.py && python train_model.py || echo "Not training model"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
