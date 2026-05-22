from pydantic import  BaseModel , ConfigDict , EmailStr , Field
from typing import Optional ,Literal 


class MemberCreate(BaseModel):
    name : str
    email : EmailStr 
    phone : str = Field(min_length=10,max_length=10)
    password : str 
    membership_type: Literal["basic","premium"]="basic"

    # @field_validator("mobile")
    # @classmethod
    # def mobile_must_be_digits(cls,v):
    #     if not v.isdigit():
    #         raise ValueError("Mobile must contain only digits")
    #     return v

class MemberResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int 
    name : str 
    email : EmailStr
    phone :str 
    membership_type:str 


class LoginRequest(BaseModel):
    email : EmailStr
    password:str 

class TokenResponse(BaseModel):
    access_token : str 
    token_type : str  = "bearer"