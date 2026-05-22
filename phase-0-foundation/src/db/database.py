from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , declarative_base 
from src.core.config import settings

Base = declarative_base()

engine = create_engine(settings.database_url)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = session()
    try:
        yield db 
    finally :
        db.close()

