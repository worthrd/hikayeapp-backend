from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlmodel import Session, select, SQLModel
from typing import List, Optional

from hikayeapp_backend.database import get_session
from hikayeapp_backend.models.user import User
from hikayeapp_backend.services.auth_service import AuthService

router = APIRouter(prefix="/users", tags=["Users"])

class ChildRead(SQLModel):
    id: int
    name: str
    age: str

    class Config:
        orm_mode = True


class UserRead(SQLModel):
    id: int
    email: str
    name: Optional[str]
    surname: Optional[str]
    subscribed: bool
    story_read: int
    story_listened: int
    children: List[ChildRead] = []

    class Config:
        orm_mode = True

@router.get("/", response_model=List[User])
def list_users(session: Session = Depends(get_session), current_user: User = Depends(AuthService.get_current_user)):
    users = session.exec(select(User)).all()
    return users


@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(AuthService.get_current_user)):
    return current_user


@router.put("/me", response_model=User)
def update_me(
    name: str = Form(None),
    surname: str = Form(None),
    subscribed: bool = Form(None),
    avatar: UploadFile = File(None),
    current_user: User = Depends(AuthService.get_current_user),
    session: Session = Depends(get_session),
):

    if name is not None:
        current_user.name = name
    if surname is not None:
        current_user.surname = surname
    if subscribed is not None:
        current_user.subscribed = subscribed
    if avatar is not None:
        current_user.avatar = avatar.file.read()

    session.add(current_user)
    session.commit()
    session.refresh(current_user)

    return current_user


@router.delete("/me")
def delete_me(
    current_user: User = Depends(AuthService.get_current_user),
    session: Session = Depends(get_session),
):

    session.delete(current_user)
    session.commit()
    return {"msg": "User deleted successfully"}
