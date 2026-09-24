# PostgreSQL

install PostgreSQL: `brew install postgresql`

## in PostgreSQL

- psql postgres

postgres=# `CREATE DATABASE fastapi_db;`
CREATE DATABASE

> entry to db 
\c fastapi_db

You are now connected to database "fastapi_db" as user "softzino".

> list or roles dekhar jonno

fastapi_db=# \du

> je kono path theke 

psql -U softzino -d fastapi_db

fastapi_db=# SELECT current_user;
current_user
--------------
softzino
(1 row)

fastapi_db=# show port;
port
------
5432
(1 row)