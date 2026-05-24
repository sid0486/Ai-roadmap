from pydantic import BaseModel,ConfigDict 
from datetime import datetime

class TaskCreate(BaseModel):
    title : str

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id :int
    title : str
    completed : bool 
    streak : int 
    last_completed: datetime | None
    created_at : datetime
    user_id : int


class TaskUpdate(BaseModel):
    title : str
    completed : bool



