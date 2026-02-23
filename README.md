# python-sqlalchemy
Here is a clean and professional **README.md** for your `python-sqlalchemy` project 👇
You can copy this directly into your `README.md`.

---

# 🐍 Python SQLAlchemy Tutorial Project

A simple **CLI-based Task Management System** built using **SQLAlchemy ORM** and **SQLite**.

This project demonstrates:

* ✅ Database connection using SQLAlchemy
* ✅ ORM Model creation
* ✅ One-to-Many relationships
* ✅ CRUD Operations
* ✅ Exception handling (`IntegrityError`)
* ✅ SQLite database integration

---

## 📚 Technologies Used

* Python 3
* SQLAlchemy ORM
* SQLite
* Virtual Environment (venv)

---

## 🗂 Project Structure

```text
alchemyTutorial/
│
├── main.py
├── tasks.db
├── .env/
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Create Virtual Environment

```bash
python -m venv .env
```

## 2️⃣ Activate Virtual Environment (Windows PowerShell)

```bash
.\.env\Scripts\Activate.ps1
```

## 3️⃣ Install Required Package

```bash
pip install sqlalchemy
```

## 4️⃣ Run the Application

```bash
python .\main.py
```

---

# 🗄 Database Configuration

The application uses **SQLite**:

```python
engine = create_engine('sqlite:///tasks.db', echo=True)
```

* Database file: `tasks.db`
* Automatically created on first run
* SQL queries are shown in terminal (`echo=True`)

---

# 🧱 Database Models

## 👤 User Model

* `id` (Primary Key)
* `name` (Required)
* `email` (Unique, Required)
* Relationship: One user can have multiple tasks

## 📌 Task Model

* `id` (Primary Key)
* `title` (Required)
* `description`
* `user_id` (Foreign Key → users.id)
* Relationship: Each task belongs to one user

### Relationship Type:

**One-to-Many (User → Tasks)**

---

# 🔄 Features & CRUD Operations

### ✅ Add User

* Prevents duplicate emails
* Handles database integrity errors

### ✅ Add Task

* Adds task to an existing user

### ✅ Query Users

* Displays all users in the database

### ✅ Query Tasks

* Displays all tasks for a specific user

---

# 🖥 CLI Menu Options

```text
1. Add User
2. Add Task
3. Query Users
4. Query Tasks
5. Update User
6. Delete User
7. Delete Task
8. Exit
```

(Current implementation includes options 1–4 and Exit.)

---

# 🧠 Concepts Practiced

* SQLAlchemy ORM
* `create_engine`
* `declarative_base`
* `sessionmaker`
* Relationships (`relationship`, `ForeignKey`)
* Exception handling with `IntegrityError`
* Basic CLI interaction
* Clean function-based structure

---

# 🎯 Learning Purpose

This project is built for learning and practicing:

* SQLAlchemy ORM fundamentals
* Database relationships
* Python database applications
* Backend development concepts

---

# 👨‍💻 Author

Sajal Das

