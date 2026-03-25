from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db

router = APIRouter(prefix="/moods", tags=["Moods"])


@router.post("/", response_model=schemas.MoodResponse)
def create_mood(mood: schemas.MoodCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == mood.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_mood = models.MoodEntry(
        user_id=mood.user_id,
        mood=mood.mood,
        note=mood.note
    )

    db.add(new_mood)
    db.commit()
    db.refresh(new_mood)

    return new_mood


@router.get("/{user_id}", response_model=list[schemas.MoodResponse])
def get_user_moods(user_id: int, db: Session = Depends(get_db)):
    moods = db.query(models.MoodEntry).filter(models.MoodEntry.user_id == user_id).all()
    return moods