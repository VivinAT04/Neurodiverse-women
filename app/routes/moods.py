from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.dependencies import get_current_user

router = APIRouter(prefix="/moods", tags=["Moods"])


@router.post("/", response_model=schemas.MoodResponse)
def create_mood(
    mood: schemas.MoodCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_mood = models.MoodEntry(
        user_id=current_user.id,
        mood=mood.mood,
        note=mood.note
    )

    db.add(new_mood)
    db.commit()
    db.refresh(new_mood)

    return new_mood


@router.get("/", response_model=list[schemas.MoodResponse])
def get_user_moods(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    moods = db.query(models.MoodEntry).filter(models.MoodEntry.user_id == current_user.id).all()
    return moods