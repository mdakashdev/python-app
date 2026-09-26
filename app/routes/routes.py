from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controller.register_controller import store
from app.schemas.auth import RegisterRequest

router = APIRouter(
    prefix="/api"
)

@router.post("/reg")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
     #data = await request.json()
     #print(data)
    return store(request, db)


# route create : 23 Sep 26

# Route::get('/users', function() { return "test text"} );
@router.get("/users")
def get_users():
    return {
        "message": "successfully message from test api"
    }
