from typing import Optional
from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class ChildBase(BaseModel):
    name:str
    age:str
    avatar:Optional[bytes] = None
    model_config = SettingsConfigDict(from_attributes=True)

class ChildCreate(ChildBase):
    pass

class ChildRead(ChildBase):
    id: int

class ChildUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    avatar: Optional[bytes] = None
    user_id: Optional[int] = None

 
