from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.db import get_db

router = APIRouter(prefix="/assistant", tags=["Assistant"])


@router.get("/{user_id}")
def get_assistant_response(user_id: int, db: Session = Depends(get_db)):
    # get latest mood
    latest_mood = (
        db.query(models.MoodEntry)
        .filter(models.MoodEntry.user_id == user_id)
        .order_by(models.MoodEntry.created_at.desc())
        .first()
    )

    # get tasks
    tasks = db.query(models.Task).filter(models.Task.user_id == user_id).all()

    pending_tasks = [t for t in tasks if t.status == "pending"]

    response = {}

    # mood-based suggestion
    if latest_mood:
        if latest_mood.mood.lower() == "anxious":
            response["mood_advice"] = "Take a short break. Try a 2-minute breathing exercise."
        elif latest_mood.mood.lower() == "sad":
            response["mood_advice"] = "Consider going for a short walk or talking to a friend."
        else:
            response["mood_advice"] = "You're doing good. Keep going!"

    # task-based suggestion
    if len(pending_tasks) > 3:
        response["task_advice"] = "You have many pending tasks. Start with one small task."
    elif len(pending_tasks) == 0:
        response["task_advice"] = "Great job! All tasks completed 🎉"
    else:
        response["task_advice"] = "Keep working on your tasks step by step."

    return response