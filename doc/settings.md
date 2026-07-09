# Step 1 — Python Installation Verify
# Step 2 — একটা project folder তৈরি করো
# Step 3 — Virtual Environment (`venv`)
## Step 4 — Activate Virtual Environment


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

# Step 3 — Virtual Environment (`venv`)

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

## Step 4 — Activate Virtual Environment

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



### ছোট্ট নোট

macOS-এ, ls -la
আমরা macOS-এ `python3` এবং `pip3` command ব্যবহার করব। পরে চাইলে shell alias দিয়ে `python` ও `pip` ব্যবহার করা যায়, কিন্তু শেখার শুরুতে default command-ই ব্যবহার করব যাতে environment নিয়ে কোনো confusion না হয়।
