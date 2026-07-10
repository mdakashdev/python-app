## Step 1 — Python Installation Verify
## Step 2 — একটা project folder তৈরি করো
## Step 3 — Make Virtual Environment (`venv`)
## Step 4 — Activate Virtual Environment
## Step 5 — FastAPI Install
## Step 6 — Project Structure তৈরি
## Step 7 — `main.py` তৈরি
## .venv নতুন করে তৈরি করি


# Step 1 — Python Installation Verify

Terminal এ Run করো:

```bash
python3 --version
```

তারপর:

```bash
pip3 --version
```

---

## কেন?

Mac-এ অনেক সময় `python` command থাকে না, `python3` ব্যবহার করতে হয়।

আমরা আগে verify করব:

* Python install আছে কিনা
* Version কত
* pip install আছে কিনা

---

# Step 2 — একটা project folder তৈরি করো

```bash
mkdir python-auth-api
cd python-auth-api
```

Perfect. 👍 Project folder ready.

---

# Step 3 — Make Virtual Environment (`venv`)

Run করো:

```bash
python3 -m venv .venv
```

তারপর check করো:

```bash
ls
```

তুমি `.venv` নামে একটা folder দেখতে পাবে।

---

এটা macOS-এর একদম normal behavior। 😊

কারণ `.venv` একটি **hidden folder**। যেসব file/folder-এর নাম `.` (dot) দিয়ে শুরু হয়, `ls` ডিফল্টভাবে সেগুলো দেখায় না।

দেখতে চাইলে run করো:

```bash
ls -la
```

তাহলে `.venv` দেখতে পাবে।

---

# Step 4 — Activate Virtual Environment

Run করো:

```bash
source .venv/bin/activate
```

যদি successful হয়, terminal prompt-এর শুরুতে এমন দেখাবে:

```bash
(.venv)
```

উদাহরণ:

```bash
(.venv) MacBook-Pro python-auth-api %
```

## Step 5 — FastAPI Install

```bash
pip install fastapi uvicorn

or 

python -m pip install fastapi uvicorn
```
>আমি এখানে pip install না দিয়ে python -m pip ব্যবহার করছি, কারণ এতে নিশ্চিত হয় যে এই venv-এর Python-এর pip-ই ব্যবহার হচ্ছে।

এখানে আমরা fastapi এবং uvicorn একসাথে install করছি।

- FastAPI → Web Framework
- Uvicorn → ASGI Server (যেটা application run করবে)


তুমি এখানে একটা important জিনিস শিখলে:

```bash
python -m pip install fastapi uvicorn
```

এটা ব্যবহার করা ভালো practice, কারণ এটা নিশ্চিত করে:

```
Current Python
        ↓
Current Environment (.venv)
        ↓
Install Package
```

---


# Step 6 — Project Structure তৈরি

Laravel-এর সাথে মিল রেখে আমরা structure বানাবো।

তোমার project এখন:

```
python-auth-api/
│
├── .venv/
│
└──
```

এখন `app` folder এবং ভিতরের folder তৈরি করো।

Terminal-এ চালাও:

```bash
mkdir app
```

তারপর:

```bash
mkdir app/api app/services app/repositories app/models app/schemas app/core app/database
```

---

তারপর আমরা এই file গুলো বানাবো:

```
app/
│
├── main.py
│
├── api/
│   └── auth.py
│
├── services/
│   └── auth_service.py
│
├── repositories/
│   └── user_repository.py
│
├── models/
│   └── user.py
│
├── schemas/
│   └── auth.py
│
├── core/
│   └── security.py
│
└── database/
    └── connection.py
```

এটা Laravel-এর:

```
Controller
Service
Repository
Model
Request
Resource
```

এর Python version হবে।


---

# Step 7 — `main.py` তৈরি

>আমরা প্রথম `main.py` বানাবো এবং তোমার প্রথম FastAPI server run করব।

Laravel-এ যেমন entry point:

```bash
php artisan serve
```

চালালে Laravel application boot হয়।

FastAPI-তে আমাদের entry point হবে:

```
app/main.py
```

---

## 1. File তৈরি করো

```
app/main.py
```

## 2. প্রথম FastAPI Application লিখো

`app/main.py` এ লিখো:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI"
    }
```

---

এখন একটু বুঝি:

### Laravel:

```php
Route::get('/', function(){
    return "Hello";
});
```

### FastAPI:

```python
@app.get("/")
def home():
```

এখানে:

* `@app.get("/")` → Route define করছে
* `home()` → Controller method-এর মতো কাজ করছে
* `return dict` → JSON response হবে

---

# Step 8 — Server Run

Project root-এ থাকো: python-auth-api/

তারপর চালাও:

```bash
uvicorn app.main:app --reload

or 

python -m uvicorn app.main:app --reload
```

এখানে:

```
app.main
```

মানে:

```
app folder
   |
   main.py
```

আর:

```
:app
```

মানে:

```python
app = FastAPI()
```

---

Successful হলে এমন দেখাবে:

```
Uvicorn running on http://127.0.0.1:8000
```

---



# .venv নতুন করে তৈরি করি

Step 1 — venv deactivate করো

Run: deactivate তাহলে (.venv) চলে যাবে।

deactivate kore Notun kore setup

Step 1 — venv deactivate করো

Run:

```bash
deactivate
```

Step 2 — পুরানো venv delete করো

তোমার project folder-এর ভিতরে থাকো:

```bash
rm -rf .venv
```

---

Step 3 — নতুন venv তৈরি করো

```bash
python3 -m venv .venv
```

---

Step 4 — Activate করো

```bash
source .venv/bin/activate
```

---

Step 5 — এবার check করো

```bash
which python
which pip

```

দুটোর output `.venv/bin/` দেখানো উচিত।

তারপর:

```bash
pip install fastapi uvicorn
```

---






### ছোট্ট নোট

macOS-এ, ls -la
আমরা macOS-এ `python3` এবং `pip3` command ব্যবহার করব। পরে চাইলে shell alias দিয়ে `python` ও `pip` ব্যবহার করা যায়, কিন্তু শেখার শুরুতে default command-ই ব্যবহার করব যাতে environment নিয়ে কোনো confusion না হয়।
