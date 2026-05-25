from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.user_model import User
from src.schemas.user_schema import UserCreate, UserResponse, Login
from src.auth.security import get_password_hash, verify_password, create_token

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=dict)
def login_user(user: Login, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    # Unified error message to prevent user enumeration attacks
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}