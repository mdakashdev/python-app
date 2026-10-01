from fastapi import APIRouter, Depends
from app.controller.department_controller import get_list
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/api/department",
    tags=["Department"]
)

@router.get("/list")
def get_department_list(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
   ):
    return get_List(db)
