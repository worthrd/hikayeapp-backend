from sqlmodel import SQLModel
from typing import Optional


class UserOut(SQLModel):
    id: int
    email: str
    name: Optional[str] = None
    surname: Optional[str] = None


