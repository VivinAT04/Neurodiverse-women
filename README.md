# Aksess Backend API

## Overview

A secure FastAPI backend application that supports user authentication, mood tracking, task management, and personalized assistant responses.

## Features

- JWT Authentication (Register/Login)
- Protected routes
- Mood tracking system
- Task management system
- Assistant feedback system

## Tech Stack

- FastAPI
- Python
- SQLite
- SQLAlchemy
- python-jose
- passlib
- bcrypt

## Setup

### 1. Clone repository

git clone <your-repo-link>
cd aksess-backend

### 2. Create virtual environment

python -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create .env file

SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

### 5. Run server

uvicorn app.main:app --reload

## API Endpoints

Auth
POST /auth/register
POST /auth/login

Users
GET /users/me
GET /users/{user_id}

Moods
POST /moods/
GET /moods/

Tasks
POST /tasks/
GET /tasks/
PUT /tasks/{task_id}

Assistant
GET /assistant/

## Testing

Open Swagger UI:
http://127.0.0.1:8000/docs

## Example Flow

1. Register user
2. Login and get token
3. Click Authorize in Swagger
4. Create mood
5. Create task
6. Update task
7. Get assistant response

## Author

Vivin Anitha Thambidurai
