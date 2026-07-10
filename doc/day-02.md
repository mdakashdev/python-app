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
