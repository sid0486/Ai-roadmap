from fastapi import FastAPI
from src.routes.user_route import router as User
from src.routes.task_route import router as Task
from src.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://your-app.vercel.app",  # ← update this after Vercel deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(User, prefix="/users", tags=["Users"])
app.include_router(Task, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def home():
    return {
        "message": "Consistency Tracker API Running"
    }