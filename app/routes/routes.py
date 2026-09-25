from fastapi import APIRouter, Request
from app.controller.register_controller import store
from app.schemas.auth import RegisterRequest

router = APIRouter(
    prefix="/api"
)

@router.post("/reg")
def register(request: RegisterRequest):
#     data = await request.json()
#     print(data)
    return store(request)


# route create : 23 Sep 26

# Route::get('/users', function() { return "test text"} );
@router.get("/users")
def get_users():
    return {
        "message": "successfully message from test api"
    }
