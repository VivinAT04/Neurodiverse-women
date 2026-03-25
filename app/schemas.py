from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class MoodCreate(BaseModel):
    user_id: int
    mood: str
    note: Optional[str] = None


class MoodResponse(BaseModel):
    id: int
    user_id: int
    mood: str
    note: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    user_id: int
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    status: str


class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True