from pydantic import  BaseModel , ConfigDict
from datetime import date  
from typing import Optional 



class BorrowCreate(BaseModel): 
    book_id:int 
    member_id:int
    
class BorrowResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int 
    book_id:int 
    member_id:int
    borrowed_on: date
    returned_on:Optional[date] = None