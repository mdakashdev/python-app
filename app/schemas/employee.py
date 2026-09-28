from datetime import date
from pydantic import BaseModel, Field, EmailStr

class RequestEmployee(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    position: str = Field(min_length=3, max_length=50)
    email: EmailStr
    joining_date: date
    status: str = Field(min_length=3, max_length=10)
