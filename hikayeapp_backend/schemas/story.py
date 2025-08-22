from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class StoryBase(BaseModel):
    story: Optional[str] = None
    title: Optional[str] = None
    prompt: str
    rating: Optional[int] = None
    image: Optional[bytes] = None
    
    model_config = SettingsConfigDict(from_attributes=True)
    

class StoryCreate(StoryBase):
    pass

class StoryRead(StoryBase):
    id: int
    created_at: datetime

class StoryUpdate(BaseModel):
    story: Optional[str] = None
    title: Optional[str] = None
    prompt: Optional[str] = None
    rating: Optional[int] = None
    image: Optional[bytes] = None
    child_id: Optional[int] = None




