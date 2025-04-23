
from fastapi import FastAPI
from app.dialog_manager import generate_response

app = FastAPI()

@app.get("/chat/")
def chat(user_input: str):
    return {"response": generate_response(user_input)}
