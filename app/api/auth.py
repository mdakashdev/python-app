from fastapi import APIRouter
from app.schemas.auth import RegisterRequest

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(request: RegisterRequest):
    return {
        "message": "Register API",
        "data": request
    }

@router.post("/login")
def login():
    return {
        "message": "Hello FastAPI Login API"
    }




# এখানে RegisterRequest হবে একটা Pydantic Model।
# এই API JSON body নেবে।
# Validation করবে।
# Swagger-এ JSON schema দেখাবে।

# Request Schema Connect





# FastAPI library থেকে APIRouter import করছি।
# as like use Illuminate\Support\Facades\Route;

# এখানে একটা router object তৈরি হচ্ছে।
# as like Router::post(...)

# মানে এই router-এর সব endpoint-এর আগে /auth যোগ হবে। like - /auth/register
# as like - Route::prefix('auth')->group(function () {});

# এটা Swagger documentation-এর জন্য। পরে যখন /docs open করবে, তখন সব authentication API এক group-এর নিচে দেখাবে।
# what is ?? postman!!

# এটা decorator। /register URL-এ POST request এলে নিচের function call করো।
# এখন এটা temporary function।

# Python dictionary return করছি। FastAPI automatically এটাকে JSON বানিয়ে client-কে পাঠাবে।