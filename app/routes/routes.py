from fastapi import APIRouter
from app.controller.auth_controller import register

router = APIRouter(
    prefix="/api"
)

# route create : 23 Sep 26

# Route::get('/users', function() { return "test text"} );
@router.get("/users")
def get_users():
    return {
        "message": "successfully message from test api"
    }


@router.post("/reg")
def store():
    return register()