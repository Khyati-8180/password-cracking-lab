# 🔐 Password Cracking Lab — Streamlit Edition

A fully interactive cybersecurity lab built in **100% Python** using Streamlit.
No HTML. No JavaScript. No web experience needed.

---

## 🗂️ What's inside

```
password_lab/
├── app.py            ← the entire application (one file!)
├── requirements.txt  ← packages to install
└── README.md         ← this file
```

---

## 🚀 How to run it (baby steps)

### Step 1 — Make sure Python is installed
Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:
```bash
python --version
```
You should see `Python 3.10` or higher. If not, download it from https://python.org

---

### Step 2 — Install the required packages
In your terminal, navigate to this folder and run:
```bash
pip install -r requirements.txt
```
This installs:
- `streamlit` — the framework that turns Python into a web app
- `bcrypt`    — for the secure hashing demo in Lab 4

---

### Step 3 — Run the app
```bash
streamlit run app.py
```
Your browser will automatically open to `http://localhost:8501` 🎉

---

## 🧪 The Four Labs

| Lab | Topic | Key Concept |
|-----|-------|-------------|
| 1 | **Hashing** | MD5 / SHA-1 / SHA-256 — live hash generation + avalanche effect |
| 2 | **Wordlist Attack** | Dictionary attack simulation — watch it crack common passwords |
| 3 | **Brute Force** | Every possible combination — keyspace explosion explained |
| 4 | **Defense** | Password scoring + bcrypt + real Python code to use in production |

---

## 🐍 Python concepts used in this project

| Concept | Where it's used |
|---------|-----------------|
| `hashlib` — built-in Python module | Generating MD5, SHA-1, SHA-256 hashes |
| `itertools.product()` | Generating every combination in brute force |
| `string` module | Character sets (lowercase, digits, symbols) |
| `time` module | Measuring elapsed attack time |
| `bcrypt` library | Demonstrating secure password storage |
| Streamlit widgets | `st.text_input`, `st.button`, `st.progress`, `st.tabs` |
| f-strings | Building dynamic HTML strings for custom styling |
| List comprehensions | Building check results, tables |
| Functions with type hints | `hash_md5(text: str) -> str` |

---

## 💡 Things to try

1. In **Lab 2**, type `password` → watch it crack instantly. Then type `xK9!mZqL` → not in list.
2. In **Lab 3**, try `hi` (676 combos) vs `cat` (17,576 combos) — feel the difference.
3. In **Lab 4**, type the same password and watch the strength score change live.
4. In **Lab 4**, scroll down and try running the bcrypt code snippet in your own Python file.

---

## 🔒 Ethical note

This lab is for **educational purposes only**. Understanding how attacks work is the
foundation of building better defenses. Never use these techniques against systems
you don't own or have explicit permission to test.