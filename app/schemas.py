from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str  

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class FlowerBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class FlowerCreate(FlowerBase):
    pass

class FlowerOut(FlowerBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str