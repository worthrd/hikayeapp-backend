from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session

from hikayeapp_backend.database import get_session
from hikayeapp_backend.schemas.story import StoryRead, StoryUpdate, StoryCreate
from hikayeapp_backend.services.story_service import StoryService
from hikayeapp_backend.services.auth_service import AuthService
from hikayeapp_backend.models.user import User

router = APIRouter(prefix="/story", tags=["Story"])

@router.post("/{child_id}", response_model = StoryRead)
def create_story(child_id:int, 
                 story_to_create: StoryCreate, 
                 current_user: User = Depends(AuthService.get_current_user), 
                 session: Session = Depends(get_session)):
    return StoryService.create_story(child_id, story_to_create, session, current_user)
    
@router.get("/", response_model = List[StoryCreate])
def list_stories(session: Session = Depends(get_session), current_user: User = Depends(AuthService.get_current_user)):
    return StoryService.list_stories(session, current_user)

@router.get("/{story_id}", response_model=StoryRead)
def get_story(story_id: int,
              session: Session = Depends(get_session), 
              current_user: User = Depends(AuthService.get_current_user)):
    return StoryService.get_story(session, story_id)

@router.put("/{story_id}", response_model=StoryRead)
def update_story(story_id: int, 
                 story_to_update: StoryUpdate,
                 session: Session = Depends(get_session),
                 current_user: User = Depends(AuthService.get_current_user)):
    return StoryService.update_child(session, story_id, story_to_update)

@router.delete("/{story_id}")
def delete_story(story_id: int, 
                 session: Session = Depends(get_session), 
                 current_user: User = Depends(AuthService.get_current_user)):
    return StoryService.delete_story(session, story_id)
