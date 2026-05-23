from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from src.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime ,timedelta
from passlib.context import CryptContext
from jose import jwt 
from src.config import settings
from pwdlib import PasswordHash

ALGORITHM  = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password,hashed_password):
    return password_hash.verify(
        plain_password,
        hashed_password
    )


def create_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/Login")

def get_current_user(token:str =Depends(oauth2_scheme),db:Session=Depends(get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")

    try :
        payload = jwt.decode(token,settings.secret_key,algorithms=["HS256"])
        user_id = payload.get("sub")

        if user_id is None : 
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(user_id)).first()

    if user is None:
        raise credentials_exception

    return user     




