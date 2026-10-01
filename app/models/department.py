from datetime import date
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(300))
    head: Mapped[str] = mapped_column(String(50), unique=True)
    status: Mapped[str] = mapped_column(String(50))