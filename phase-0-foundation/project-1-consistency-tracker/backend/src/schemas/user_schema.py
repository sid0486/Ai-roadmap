from pydantic import BaseModel , ConfigDict ,EmailStr

class UserCreate(BaseModel):
    username : str 
    email : EmailStr
    password : str 

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int 
    username : str
    email : EmailStr

class Login(BaseModel): 
    email : EmailStr  
    password : str 