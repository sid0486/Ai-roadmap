from sqlalchemy import Column , Integer , String 
from src.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True)
    email = Column(String,unique=True)
    password = Column(String)