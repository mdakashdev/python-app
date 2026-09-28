from sqlalchemy.orm import Session
from app.schemas.employee import RequestEmployee
from app.models.employee import Employee



def store(data: RequestEmployee, db: Session):
    employee = Employee(
        name = data.name,
        position = data.position,
        email = data.email,
        joining_date = data.joining_date,
        status = data.status
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)

    return {
        "message": "Successfully",
        "data": employee
    }