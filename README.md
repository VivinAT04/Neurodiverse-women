# Aksess Backend

A FastAPI backend for an accessibility-focused support app designed to help neurodivergent women manage tasks, track moods, and receive assistant guidance.

## Features

- User registration and login with JWT authentication
- Password hashing for secure storage
- Mood tracking system
- Task management (create, update, view)
- Assistant suggestions based on mood and tasks
- Swagger UI for API testing
- JWT-protected routes (in progress)

## Tech Stack

- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)

## Project Structure

aksess-backend/
├── app/
│ ├── routes/
│ │ ├── auth.py
│ │ ├── users.py
│ │ ├── moods.py
│ │ ├── tasks.py
│ │ └── assistant.py
│ ├── db.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ └── crud.py
├── requirements.txt
├── README.md
└── .gitignore

## API Endpoints

Auth:

- POST /auth/register → Register new user
- POST /auth/login → Login and get JWT token

Users:

- GET /users/{user_id} → Get user details

Moods:

- POST /moods/ → Create mood entry
- GET /moods/{user_id} → Get user moods

Tasks:

- POST /tasks/ → Create task
- GET /tasks/{user_id} → Get tasks
- PUT /tasks/{task_id} → Update task

Assistant:

- GET /assistant/{user_id} → Get suggestions

## Authentication

Register:

POST /auth/register

{
"name": "Vivin",
"email": "vivin@test.com",
"password": "test1234"
}

Login:

POST /auth/login

{
"email": "vivin@test.com",
"password": "test1234"
}

Response:

{
"access_token": "your-token",
"token_type": "bearer"
}

## Run Locally

git clone https://github.com/VivinAT04/Neurodiverse-women.git  
cd Neurodiverse-women

python3 -m venv venv  
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

Open:
http://127.0.0.1:8000/docs

## Workflow

1. Register user
2. Login to get token
3. Create moods
4. Create tasks
5. Update tasks
6. Get assistant suggestions

## Assistant Logic

- If mood is anxious → suggest breathing exercise
- If many pending tasks → suggest starting small
- If tasks completed → show positive feedback

## Notes

- Passwords are hashed using bcrypt
- JWT used for authentication
- SQLite used for development
- Backend MVP ready

## Future Improvements

- Add JWT protection to routes
- Connect frontend UI
- AI-based assistant
- Environment variables for secrets
- Deploy to cloud (AWS/Render)
- Use PostgreSQL instead of SQLite

## Author

Vivin A T
