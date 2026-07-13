from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(
    title="Authentication API",
    version="1.0"
)

app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI"
    }


# auth.py থেকে router object import করছি। কিন্তু local variable-এর নাম দিলাম: auth_router

# http://127.0.0.1:8000/docs এখানেই FastAPI-এর একটা অসাধারণ feature দেখবে। Swagger UI automatically generate হবে।