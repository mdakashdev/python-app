from app.schemas.auth import RegisterRequest
from sqlalchemy.orm import Session
from app.models.user import User

def store(data: RegisterRequest, db: Session):
    user = User(
        name=data.name,
        email=data.email,
        password=data.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "successfully registration11",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }