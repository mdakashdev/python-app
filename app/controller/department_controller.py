from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.department import Department


def get_list(db: Session):
    department = db.scalars(
        select(Department)
    ).all()

    return department

