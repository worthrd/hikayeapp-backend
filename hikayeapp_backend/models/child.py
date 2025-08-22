from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum

class AgeGroup(str, Enum):
    zero_to_two = "0-2"
    two_to_four = "2-4"
    four_to_six = "4-6"
    six_to_eight = "6-8"

class Child(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str
    age: AgeGroup = Field(index = True)
    stories: List["Story"] = Relationship(back_populates="child")
    avatar: Optional[bytes] = None
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory = datetime.utcnow)
    updated_at: datetime = Field(default_factory = datetime.utcnow)
