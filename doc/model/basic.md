# Model

Project-এ এই folder/file তৈরি করুন:

```text
app/
├── database/
│   └── connection.py
├── models/
│   ├── __init__.py
│   └── user.py
```

`app/models/user.py`-তে লিখুন:

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
```

## base Model


> এটা আমাদের সব database model-এর **parent/base class**।


এই file তৈরি করুন:

```text
app/
└── database/
    ├── connection.py
    └── base.py
```

`app/database/base.py`:

```python
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
```

### এটা কী করছে?

```python
class Base(DeclarativeBase):
    pass
```

এটা আমাদের সব database model-এর **parent/base class**।

তাই `User` model-এ:

```python
class User(Base):
```

মানে:

> `User` হলো SQLAlchemy database model।

এর কারণে SQLAlchemy বুঝতে পারবে:

```text
User Model
    ↓
users table
```

### Laravel-এর সাথে মিল

Laravel-এ:

```php
class User extends Model
{
    //
}
```

Python/SQLAlchemy-তে:

```python
class User(Base):
    ...
```

Concept একই ধরনের:

```text
Laravel
User → Model → Database

FastAPI
User → SQLAlchemy Base → Database
```
