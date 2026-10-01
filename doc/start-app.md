

# python -m uvicorn app.main:app --reload

# Table create
- `alembic revision --autogenerate -m "create users table"`

# Run migration table
- `alembic upgrade head`