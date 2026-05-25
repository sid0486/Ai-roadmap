from fastapi import APIRouter,HTTPException,Depends,status
from src.database import get_db
from sqlalchemy.orm import Session
from src.models.user_model import User
from src.models.tasks_model import Task
from src.schemas.task_schema import TaskCreate,TaskResponse,TaskUpdate
from src.auth.security import get_current_user
from datetime import datetime,timedelta


router = APIRouter()


@router.get("/",response_model=list[TaskResponse])
def get_tasks(db:Session=Depends(get_db),current_user:User = Depends(get_current_user)):
    return db.query(Task).filter(Task.user_id == current_user.id).all()

@router.get("/{id}",response_model=TaskResponse)
def get_by_id(id:int,db:Session=Depends(get_db),current_user:User = Depends(get_current_user)):
    db_tasks = db.query(Task).filter(Task.id==id,Task.user_id == current_user.id).first()
    if not db_tasks:
        raise HTTPException(status_code=404,detail="task not found")
    return db_tasks

@router.post("/",response_model=TaskResponse)
def add_tasks(task:TaskCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    existing = db.query(Task).filter(Task.title == task.title ,Task.user_id == current_user.id).first()
    if existing:
        raise HTTPException(status_code=400,detail="task already exists")
    new_task = Task(
        title = task.title,
        user_id = current_user.id   

    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.put("/{id}",response_model=TaskResponse)
def update_task(id:int,task:TaskUpdate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.id == id, Task.user_id == current_user.id).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db_task.title = task.title
    db_task.completed = task.completed

    today = datetime.utcnow()

    if task.completed:
        if db_task.last_completed:
            difference = (today.date() - db_task.last_completed.date()).days
            if difference == 1:
                db_task.streak += 1
            elif difference > 1:
                db_task.streak = 1
            # Bug fix: missing else — if difference == 0 (completed twice same day),
            # streak should stay unchanged, not reset
        else:
            # First time ever completing — start streak at 1
            db_task.streak = 1

        db_task.last_completed = today  # Bug fix: was also set in the else block by mistake
    else:
        # Bug fix: resetting streak to 1 when unchecking is wrong.
        # Streak should only reset to 0 — it hasn't been completed.
        db_task.streak = 0

    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/{id}")
def delete_task(id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    db_task = db.query(Task).filter(Task.id==id,Task.user_id==current_user.id).first()
    if not db_task:
        raise HTTPException(status_code=404,detail="task not found")
    db.delete(db_task)
    db.commit()
    return {"message":"task deleted successfully"}




























