from fastapi import FastAPI
from src.routes.user_route import router as User
from src.database import Base , engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(User,prefix="/users",tags=["Users"])

@app.get("/")
def home():
    return {
        "message": "Consistency Tracker API Running"
    }