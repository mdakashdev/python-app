from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest
from app.models.user import User

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

    return {
        "message": "Login Successfully",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }

    }