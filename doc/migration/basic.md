# Migration 


## root a

alembic init alembic


## alembic/env.py

change `target_metadata`

```
from app.database.base import Base
from app.models.user import User

target_metadata = Base.metadata
```

এর মাধ্যমে Alembic জানবে:

আমাদের project-এ User নামে একটি database model আছে।

## Alembic-কে .env থেকে PostgreSQL URL nibo 

sei jonno - 


কারণ `alembic.ini`-তে default একটা placeholder থাকে:

```ini
sqlalchemy.url = driver://user:pass@localhost/dbname
```

আমরা চাই না database username/password আলাদা করে এখানে লিখতে। আমাদের already `.env` আছে।

### 1️⃣ `alembic/env.py` খুলুন

উপরে import section-এ এগুলো add করুন:

```python
import os
from dotenv import load_dotenv
```

তারপর:

```python
load_dotenv()
```

এবং `run_migrations_online()` function-এর ভিতরে `connectable = engine_from_config(...)`-এর **আগে** এই line দিন:

```python
config.set_main_option(
    "sqlalchemy.url",
    os.getenv("DATABASE_URL")
)
```


### কেন এটা করছি?

Flow হবে:

```text
.env
  ↓
DATABASE_URL
  ↓
alembic/env.py
  ↓
SQLAlchemy
  ↓
PostgreSQL
```

অর্থাৎ তোমার:

```env
DATABASE_URL=postgresql+psycopg://softzino@localhost:5432/fastapi_db
```

এই connection-টাই Alembic ব্যবহার করবে।


## migration create 

Table create - `alembic revision --autogenerate -m "create users table"`

run migration table - `alembic upgrade head`

check table - `fastapi_db=# \dt`

check specific table - `fastapi_db=# \d users`

check tables data - `fastapi_db=# select * from users;`


exit hote - \q

entry neyar jonno - psql postgres