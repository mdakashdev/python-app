from fastapi import APIRouter, Request
from app.controller.register_controller import store

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
async def register(request: Request):
    data = await request.json()
    print(data)
    return store(data)
