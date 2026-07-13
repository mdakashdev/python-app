from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register():
    return {
        "message": "Hello FastAPI Register API"
    }

@router.post("/login")
def login():
    return {
        "message": "Hello FastAPI Login API"
    }


# FastAPI library থেকে APIRouter import করছি।
# as like use Illuminate\Support\Facades\Route;

# এখানে একটা router object তৈরি হচ্ছে।
# as like Router::post(...)

# মানে এই router-এর সব endpoint-এর আগে /auth যোগ হবে। like - /auth/register
# as like - Route::prefix('auth')->group(function () {});

#এটা Swagger documentation-এর জন্য। পরে যখন /docs open করবে, তখন সব authentication API এক group-এর নিচে দেখাবে।
# what is ??

# এটা decorator। /register URL-এ POST request এলে নিচের function call করো।
# এখন এটা temporary function।

# Python dictionary return করছি। FastAPI automatically এটাকে JSON বানিয়ে client-কে পাঠাবে।