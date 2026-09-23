from fastapi import APIRouter

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
