from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6, max_length=255)

class LoginRequest(BaseModel):
    email: str
    password: str


# use Illuminate\Foundation\Http\FormRequest;
# from pydantic import BaseModel