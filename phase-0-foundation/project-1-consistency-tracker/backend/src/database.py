from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base 
from src.config import settings

Base = declarative_base()

# Railway gives postgres:// but SQLAlchemy needs postgresql://
database_url = settings.database_url
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()