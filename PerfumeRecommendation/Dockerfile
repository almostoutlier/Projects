FROM python:3.11
WORKDIR /app
ENV NAME=venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY fra_cleaned.csv .
COPY templates/ ./templates/
EXPOSE 80
CMD ["python", "app.py"]