from fastapi import APIRouter ,HTTPException , Depends
from sqlalchemy.orm import Session 
from src.database import get_db
from src.models.user_model import User
from src.schemas.user_schema import UserCreate,UserResponse,Login
from src.auth.security import get_password_hash,verify_password,create_token

router = APIRouter()



@router.post("/",response_model=UserResponse)
def register(user:UserCreate,db:Session=Depends(get_db)):
    existing = db.query(User).filter(User.email==user.email).first()
    if existing:
        raise HTTPException(status_code=400,detail="user already exists")
    hashed_password = get_password_hash(user.password) 
    new_user = User(
        username = user.username,
        email = user.email,
        password = hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.post("/login")
def login_user(user:Login,db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.email==user.email).first()
    if not user :
        raise HTTPException(status_code=404,detail="Invalid email")
    is_valid = verify_password(user.password,db_user.password)
    if not is_valid:
        raise HTTPException(status_code=401,detail="Invalid password")
    token = create_token({"sub":str(User.id)})
    return TokenResponse(access_token=token)