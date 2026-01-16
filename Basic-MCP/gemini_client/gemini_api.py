import google.generativeai as genai
import os

# Set your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_predict(prompt: str):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
