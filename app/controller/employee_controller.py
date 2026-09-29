from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.employee import RequestEmployee
from app.models.employee import Employee


def store(data: RequestEmployee, db: Session):
    existing_employee = db.scalar(
        select(Employee).where(Employee.email == data.email)
    )

    if existing_employee:
        raise HTTPException(
            status_code=422,
            detail="Email already exists"
        )

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

def get_employees(db: Session):
    employee = db.scalars(
        select(Employee)
    ).all()

    return employee


def update(id: int, data: RequestEmployee, db: Session):

    employee = db.scalar(
        select(Employee).where(Employee.id == id)
    )

    if not employee:
        return {
            "message": "Employee not found"
        }

    employee.name = data.name
    employee.position = data.position
    employee.email = data.email
    employee.joining_date = data.joining_date
    employee.status = data.status

    db.commit()
    db.refresh(employee)

    return {
        "message": "Employee updated successfully",
        "data": employee
    }


def delete(id: int, db: Session):
    employee = db.scalar(
        select(Employee).where(Employee.id == id)
    )

    if not employee:
        return {
            "message": "Employee not found"
        }

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }