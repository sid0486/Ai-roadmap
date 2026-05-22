from pydantic import BaseModel,ConfigDict,Field,field_validator,computed_field 
from typing import Optional

class ProductCreate(BaseModel):
    name:str
    description : Optional[str] = None 
    price: float
    quantity :int 

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int 
    name:str
    description : Optional[str] 
    price: float
    quantity :int 


    @computed_field
    @property
    def total_value(self) -> float:
        return self.price * self.quantity 

