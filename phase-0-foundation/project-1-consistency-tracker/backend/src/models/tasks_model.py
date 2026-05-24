from sqlalchemy import Column , Integer , String ,DateTime,Boolean,ForeignKey
from datetime import datetime
from src.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    completed = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    streak = Column(
        Integer,
        default=0
    )

    last_completed = Column(
        DateTime,
        nullable=True
    )

    user_id = Column(
        Integer,
        ForeignKey("user.id")
    )