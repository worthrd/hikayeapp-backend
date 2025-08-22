from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime


class Story(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    child_id: int = Field(foreign_key = "child.id")
    child: Optional["Child"] = Relationship(back_populates="stories")
    prompt: str
    title: str
    story: str
    rating: Optional[int] = 0
    image: Optional[bytes] = None
    created_at: datetime = Field(default_factory = datetime.utcnow)
    updated_at: datetime = Field(default_factory = datetime.utcnow)
