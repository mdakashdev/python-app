## Requirements.txt generate

`.gitignore`-এ লিখুন:

```gitignore
.venv/
__pycache__/
*.pyc
```

---

### Package-এর তালিকা কীভাবে সংরক্ষণ করবেন?

সব package লিখে রাখুন:

```bash
pip freeze > requirements.txt
```

অন্য কেউ বা নতুন কম্পিউটারে:

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

এভাবেই একই environment আবার তৈরি করা যায়।

**সারসংক্ষেপ:** `.venv` হলো project-specific Python environment। এটি **Git-এ push করা উচিত নয়**। এর পরিবর্তে `requirements.txt` (বা `pyproject.toml` ব্যবহার করলে সেটি) commit করা হয়।

# Step 9 — Route আলাদা করা (APIRouter)



# Step 2 — include_router()

আমরা auth.py-তে router বানালাম।
main.py থেকে register করতে হবে।

bootstrap/app.php
↓
routes/api.php load করে

main.py
↓
include_router()
↓
auth.py

# step 4: এটাই Pydantic।
public function register(RegisterRequest $request)  অর্থাৎ request body validate হচ্ছে।

equivalent 

class RegisterRequest(BaseModel): এটাই Pydantic।




এখানেই একটা নতুন Python Concept আসবে

তুমি প্রথমবার দেখবে:

class RegisterRequest(BaseModel):

এখানে তিনটা নতুন জিনিস আছে:

class
BaseModel
Type Hint (name: str, email: EmailStr)

আমি এগুলোর প্রতিটা আলাদা করে explain করব।

Request Schema Connect


# database

python -m pip install sqlalchemy

python -m pip install pydantic-settings


config/database.php
