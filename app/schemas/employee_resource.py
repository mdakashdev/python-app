from datetime import date
from pydantic import BaseModel

class EmployeeResource(BaseModel):
    id: int
    name: str
    position: str
    email: str
    joining_date: date
    status: str

    model_config = {
        "from_attribute": True
    }