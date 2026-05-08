from pydantic import BaseModel, Field
from typing import Optional

# Common fields that are shared by other schemas
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    is_offer: Optional[bool] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    is_offer: Optional[bool] = None

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True