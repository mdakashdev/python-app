phthon, fastAPi, Flask, uvicorn, pip, venv, activate
Pydantic, Injection, passlib
requrement, .toml, activate, project run, 





question - 
 1. Swagger kivabe open korbo ?
 /docs open korlei - peye jabo.
 http://127.0.0.1:8000/docs

 2. postman theke call kora jai.

 3. PostgreSQL ki dekha jai kon interface a  


python is programming language,
fastAPI is a modern web framework
flask is light weight web framework
uvirorn hocche server / ASGI Server ; as like php aritsan server
pip hocche - package installer ; as like composer
venv hocche - virtual environment ; as like vendor
activate hocche - ei project pip & python babohar koro.
Request Validation = Pydantic
Middleware = Injection
Hash::make() = passlib / bcrypt
Resource = Response Model
activate korlam source diye, now ekhon .venv diye pabo.
main.py run korbo - python -m uvicorn app.main:app --reload
package er talika create kora jai. pip freeze diye; ja diye notun vabe project setup & install kora jai.





EndPoint :
- /users


1. route create & trigger from postman
2. controller crete 
3. db setup 
4. model create
4. migration create 
    se jonno root a : `alembic init alembic` then setup env.py and alembic.ini
    then table create - `alembic revision --autogenerate -m "create users table"`
    run migration - `alembic upgrade head`
5. DB Session তৈরি
6. Connect GUI using tableplus
7. `Request` : now, request recive korbo as like http request
    se jonno - json data pathabo postman theke, aar Request import korlei hobe,
    aar jodi formdata use korte cai tobe, python-multipart eita install korte hobe i think.
8. terminal a data dekhar jonno - print() as like dd() but stop hobe na
9. `RequestFile` : now, request file create kore, validation korbo. 
    se jonno pydantic install korte hobe, and pydantic theke BaseModel use kore validation dite hobe.
    email validator er jonno - `pip install "pydantic[email]"` install kora lagbe.
    akta request file create korbo, schemas folder a like auth.py er maddhe - RegisterRequest create korbo.
10. 





















