from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controller.register_controller import store
from app.schemas.auth import RegisterRequest
from app.controller.employee_controller import store, list, update, delete
from app.schemas.employee import RequestEmployee

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


@router.post("/employee/create")
async def create_employee(
    request: RequestEmployee,
    db: Session = Depends(get_db)
    ):
    return store(request, db)


@router.get("/employee")
def get_employee(db: Session = Depends(get_db)):
    return list(db)

@router.put("/employee/{id}")
def update_employee(
        id: int,
        request: RequestEmployee,
        db: Session = Depends(get_db)
    ):
    return update(id, request, db)


@router.delete("/employee/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    return delete(id, db)



# route create : 23 Sep 26

# Route::get('/users', function() { return "test text"} );
@router.get("/users")
def get_users():
    return {
        "message": "successfully message from test api"
    }
