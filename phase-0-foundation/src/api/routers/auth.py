from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session 
from src.db.database import get_db
from src.db import models
from src.schema.members import MemberCreate,MemberResponse,LoginRequest,TokenResponse
from src.core.security import hash_password, create_token , verify_password


router = APIRouter()


@router.post("/register",response_model=MemberResponse)
def register(member:MemberCreate ,db:Session=Depends(get_db)):
    is_User = db.query(models.Member).filter(models.Member.name==member.name).first()
    if is_User:
        raise HTTPException(status_code=400,detail="username already exists")

    is_email = db.query(models.Member).filter(models.Member.email==member.email).first()
    if is_email:
        raise HTTPException(status_code=400 , detail="email already exists")

    hash = hash_password(member.password)

    new_user = models.Member(
    name=member.name,
    email=member.email,
    password=hash,
    phone=member.phone,
    membership_type=member.membership_type
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login",response_model=TokenResponse)
def login(member:LoginRequest,db:Session=Depends(get_db)):
    User = db.query(models.Member).filter(models.Member.email==member.email).first()
    if not User:
        raise HTTPException(status_code=401,detail="You Entered Wrong Username!!")

    if not verify_password(member.password,User.password):
        raise HTTPException(status_code=401,detail="You Entered Wrong Username!!")

    token = create_token({"sub": str(User.id)})
    return TokenResponse(access_token=token) 

    

