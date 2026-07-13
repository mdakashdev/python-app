# Python 
> Python is a programming language

## What is FastAPI
>FastAPI হলো Python-এর framework।

> FastAPI হলো Python-এর একটা modern web framework, যা দিয়ে REST API বানানো হয়।

Laravel যেমন PHP-এর framework।

## Uvicorn কী?
>Server হচ্ছে Uvicorn।  

Uvicorn → ASGI Server (যেটা application run করবে)

>FastAPI নিজে server না। FastAPI শুধু framework।

Laravel-এ, php artisan serve (PHP-এর server start হয়।)
```text
Laravel
↓
PHP Built-in Server
```

Python-এ, uvicorn app.main:app (Uvicorn server start করে।)
```text
FastAPI
↓
Uvicorn
```
Client-এর request প্রথমে Uvicorn receive করে। তারপর FastAPI-এর কাছে পাঠায়।

## What is pip ?
**`pip` = Python Package Installer**

যেমন Laravel/PHP-তে:

```bash
composer require laravel/sanctum
```

তেমনি Python-এ:

```bash
pip3 install fastapi
```

অর্থাৎ `pip` দিয়ে Python package/library install, update এবং remove করা হয়।

---

## What is `venv` ?

`venv` = **Virtual Environment**

এটা project-এর জন্য আলাদা Python environment তৈরি করে।

Laravel-এ যেমন প্রতিটি project-এর নিজস্ব `vendor/` folder থাকে, তেমনি Python-এ `venv` project-এর dependencies আলাদা রাখে।

---

### `activate` আসলে কী করে?

এটা Python install করে না, `venv`-এর ভিতরে ঢুকেও না।

এটা শুধু terminal-কে বলে:

> **"এখন থেকে এই project-এর Python এবং pip ব্যবহার করো।"**

উদাহরণ: Activate করার আগে:

```bash
which python3
```

Output হতে পারে: /Library/Frameworks/Python.framework/Versions/3.12/bin/python3

Activate করার পরে:

```bash
which python
```

Output হবে: .../python-auth-api/.venv/bin/python

অর্থাৎ এখন থেকে:

* `python` → `.venv`-এর Python
* `pip` → `.venv`-এর pip

এটাই virtual environment-এর মূল উদ্দেশ্য।

---



## My Philosophy
>Laravel a `api authentication` kichu endpoint korechi, same api endpoint gulo python a korbo, aar relate korar try korbo sathe learn korbo.

>"Laravel er একই problem Python ecosystem দিয়ে solve করব"

তাহলে এটা শেখার অন্যতম সেরা উপায়।

## কেন এটা ভালো?

তোমার কাছে already problem definition আছে।

তুমি জানো— Register কী করে , Login কী করে

অর্থাৎ এখন তোমাকে business logic নিয়ে ভাবতে হবে না।

তোমার focus থাকবে—  Python ecosystem কিভাবে একই কাজ করে?

এতে cognitive load অনেক কমে যাবে।

## আমি যেভাবে করতাম

Laravel

```Laravel
Controller
↓
Service
↓
Repository
↓
Model
```

Python (FastAPI)

```text
app/
    api/
        auth.py
    services/
        auth_service.py
    repositories/
        user_repository.py
    schemas/
        auth.py
    models/
        user.py
    core/
        security.py
        auth.py
    database.py
main.py
```

দেখবে structure অনেক familiar লাগবে।

## একই API এক এক করে বানাও

Laravel - POST /register

তারপর FastAPI - POST /register

এভাবে একটার পর একটা।

## প্রতিটা endpoint বানানোর সময় প্রশ্ন করবে

- Laravel-এ Request Validation 
- Python-এ? Pydantic 
- Laravel - Middleware 
- Python? Dependency Injection 
- Laravel - Hash::make()
- Python? passlib / bcrypt 
- Laravel - Auth::user()
- Python? Current User Dependency 
- Laravel - Repository 
- Python? Repository Pattern 
- Laravel - Resource 
- Python? Response Model

> এভাবে comparison করলে অনেক দ্রুত শিখবে।




### endpoint in router

Laravel 
>Route::get('/users', ...)

FastAPI
```text
@app.get("/users")
def users()
    return []
```

FastAPI internally
```text
Receive Request
↓
Find Route
↓
Call Function
↓
Convert JSON
↓
Return Response
```

---

# তোমার Laravel experience অনুযায়ী

এভাবে মনে রাখো:

| Laravel       | Python               |
| ------------- | -------------------- |
| PHP           | Python               |
| Laravel       | FastAPI              |
| artisan serve | uvicorn              |
| Route         | @app.get()           |
| Controller    | Function / APIRouter |
| Request       | Pydantic             |
| Resource      | Response Model       |
| Middleware    | Middleware / Depends |
| Service       | Service              |
| Repository    | Repository           |

---

# Settings.md
>ekhane project setup er manual acche


# Achievement

**প্রথম FastAPI application successfully run করেছো।**

এখন পর্যন্ত তুমি যা করেছো:

```text
✅ Python environment ready
✅ Virtual Environment (`.venv`) তৈরি
✅ FastAPI install
✅ Uvicorn install
✅ Project structure তৈরি
✅ `main.py` তৈরি
✅ FastAPI server run
✅ Browser থেকে JSON response পাওয়া
```
---

এখন একটু concept clear করি।

তোমার flow এখন:

```
Browser / Postman
        |
        |
        v
    Uvicorn
        |
        |
        v
    FastAPI
        |
        |
        v
    main.py
        |
        |
        v
    home()
        |
        |
        v
    JSON Response
```

---

Laravel-এর সাথে compare:

### Laravel

```
Request
  |
Route (api.php)
  |
Controller
  |
return response()
```

### FastAPI

```
Request
  |
@app.get()
  |
Function
  |
return dict
```

---
