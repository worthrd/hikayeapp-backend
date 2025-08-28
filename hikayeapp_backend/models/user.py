from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class User(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    email: str = Field(index = True, unique = True, nullable = False)
    name: Optional[str] = None
    surname: Optional[str] = None
    subscribed: bool = False
    avatar: Optional[bytes] = None
    story_read: int = 0
    story_listened: int = 0
    children: List["Child"] = Relationship(back_populates="user")
    hashed_password: str = Field(nullable=False)
    created_at: datetime = Field(default_factory = datetime.utcnow)
    updated_at: datetime = Field(default_factory = datetime.utcnow)
