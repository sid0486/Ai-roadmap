from pydantic import BaseModel,ConfigDict
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    completed: bool = False  # ← add this


class TaskUpdate(BaseModel):          # better practice: separate schema for updates
    title: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    streak: int
    last_completed: Optional[datetime] = None
    user_id: int

    model_config = ConfigDict(from_attributes = True)