from typing import Optional
from pydantic import BaseModel, EmailStr

from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlmodel import Session, select

from hikayeapp_backend.database import get_session
from hikayeapp_backend.models.user import User
from hikayeapp_backend.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

class UserRead(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    surname: Optional[str] = None

@router.post("/register")
def register_user(user_create: UserCreate, session: Session = Depends(get_session)):

    query = select(User).where(User.email == user_create.email)
    existing_user = session.exec(query).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    hashed_password = AuthService.get_password_hash(user_create.password)
    user = User(email=user_create.email, 
                name=user_create.name, 
                surname=user_create.surname, 
                hashed_password=hashed_password
    )

    session.add(user)
    session.commit()
    session.refresh(user)
        
    token = AuthService.create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login")
def login_user(user_login: UserRead, session: Session = Depends(get_session)):

    query = select(User).where(User.email == user_login.email)
    user = session.exec(query).first()

    if not user or not AuthService.verify_password(user_login.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = AuthService.create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/refresh")
def refresh_token(current_user: User = Depends(AuthService.get_current_user)):
    token = AuthService.create_access_token({"sub": str(current_user.id)})
    return {"access_token": token, "token_type": "bearer"}



