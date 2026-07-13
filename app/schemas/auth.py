from pydantic import BaseModel

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str


# use Illuminate\Foundation\Http\FormRequest;
# from pydantic import BaseModel