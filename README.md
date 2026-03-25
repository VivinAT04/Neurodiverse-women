# Aksess Backend 🚀

A backend system for an accessibility-focused productivity and emotional support app.

---

## 🔹 Features

- User management (create & fetch users)
- Mood tracking (log and retrieve moods)
- Task management (create, update, track tasks)
- Assistant recommendations based on mood and tasks

---

## 🧠 Tech Stack

- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

---

## 📡 API Endpoints

### 👤 Users

- POST /users/
- GET /users/{user_id}

### 😊 Moods

- POST /moods/
- GET /moods/{user_id}

### 📋 Tasks

- POST /tasks/
- GET /tasks/{user_id}
- PUT /tasks/{task_id}

### 🤖 Assistant

- GET /assistant/{user_id}

---

## ⚙️ How to Run Locally

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```
