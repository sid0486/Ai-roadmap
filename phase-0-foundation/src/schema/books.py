from pydantic import BaseModel,ConfigDict
from typing import Optional 

class BookCreate(BaseModel):
    title:str 
    author:str
    genre:str
    total_copies:int 

class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    title :str
    author :str
    genre : str
    total_copies:int 

