import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv

from sqlalchemy import select
from sqlalchemy.orm import Session


from app.schemas.auth import LoginRequest
from app.models.user import User

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = "HS256"


def create_access_token(user_id: int):
    payload =  {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

    return token




def login(request: LoginRequest, db: Session):
    user = db.scalar(
        select(User).where(User.email == request.email)
    )

    if not user:
        return {
            "message": "Invalid email or password"
        }

    if user.password != request.password:
        return {
            "message": "Invalid email or password"
        }

    token = create_access_token(user.id)

    return {
        "message": "Login Successfully",
        "token": token,
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }

    }