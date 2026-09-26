# Insert

প্রথমে আমরা শুধু get_db() কীভাবে Controller-এ পৌঁছাবে সেটা করব।

- laravel a model diye insert kortam, aar db er kono kichu lagto na, but ekhane route db session nite holo keno
- controller a User model nilam and db.add diye insert kore dilam


- এখানে User হলো Eloquent Model।

- Laravel-এর Eloquent আগে থেকেই application-এর database connection/configuration-এর সাথে connected থাকে।

```python
from app.schemas.auth import RegisterRequest
from sqlalchemy.orm import Session
from app.models.user import User

def store(data: RegisterRequest, db: Session):
    user = User(
        name=data.name,
        email=data.email,
        password=data.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "successfully registration11",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }
```

db session neya 

```python
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controller.register_controller import store
from app.schemas.auth import RegisterRequest

router = APIRouter(
    prefix="/api"
)

@router.post("/reg")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
     #data = await request.json()
     #print(data)
    return store(request, db)
```

# Later
- password hashing