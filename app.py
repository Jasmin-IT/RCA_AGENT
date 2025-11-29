import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()


class Query(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "Agent API is running!"}


@app.post("/predict")
def predict(user: Query):
    try:
        response = model.generate_content(user.query)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
