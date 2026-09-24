# Database 

## PostgreSQL 

amra PostgreSQL install korbo - see @ psql/setup.md

## Migration 

install - `pip3 install alembic`


## work with database - SQLAlchemy

install - `pip3 install sqlalchemy`

ja database er connection create korar somay `engine` & `sessionmaker` bananor jonno kaje lage.


## Python driver

install - `pip3 install psycopg` or `python -m pip install "psycopg[binary]"`

psycopg → PostgreSQL-এর Python driver


# Need to Setup 

## create db

after PostgreSQL install, database create 

```bash
psql postgres
```

- ei rokom `postgres=#` interface pabo. then 

```bash
 CREATE DATABASE fastapi_db;
```

database select er jonno 

```bash
\c fastapi_db
```

caile jekono path theke db te in kora jai.

```bash
psql -U softzino -d fastapi_db
```

## .env create 

project root .env create korbe.

```dotenv
DATABASE_URL=postgresql+psycopg://softzino@localhost:5432/fastapi_db
```

eita connection theke or onno jaiga theke read korar jonno - dotenv install korte hobe

install - `pip3 install python-dotenv`

## connection create 

database/connection.py

```text
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def test_database_connection():
    try:
        with engine.connect() as connection:
            print("Database connected successfully!")
    except Exception as e:
        print("Database connection failed!")
        print(e)
```

database connection hoyeche kina, seta dekhar jonno - test_database_connection ei name akta method create korlam

## register connection in main.py

```text
from app.database.connection import test_database_connection

test_database_connection();
```