from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session

from hikayeapp_backend.database import get_session
from hikayeapp_backend.schemas.child import ChildRead, ChildUpdate, ChildCreate
from hikayeapp_backend.services.child_service import ChildService
from hikayeapp_backend.services.auth_service import AuthService
from hikayeapp_backend.models.user import User

router = APIRouter(prefix="/children", tags=["Children"])

@router.post("/", response_model = ChildRead)
def create_child(child_create: ChildCreate, 
                 current_user: User = Depends(AuthService.get_current_user), 
                 session: Session = Depends(get_session)):
    return ChildService.create_child(session, child_create, current_user)
    
@router.get("/", response_model = List[ChildCreate])
def list_children(session: Session = Depends(get_session), current_user: User = Depends(AuthService.get_current_user)):
    return ChildService.list_children(session, current_user)

@router.get("/{child_id}", response_model=ChildRead)
def get_child(child_id: int,session: Session = Depends(get_session), current_user: User = Depends(AuthService.get_current_user)):
    return ChildService.get_child(session, child_id)

@router.put("/{child_id}", response_model=ChildRead)
def update_child(child_id: int, 
                 child_to_update: ChildUpdate,
                 session: Session = Depends(get_session),
                 current_user: User = Depends(AuthService.get_current_user)):
    return ChildService.update_child(session, child_id, child_to_update)

@router.delete("/{child_id}")
def delete_child(child_id: int, 
                 session: Session = Depends(get_session), 
                 current_user: User = Depends(AuthService.get_current_user)):
    return ChildService.delete_child(session, child_id)
