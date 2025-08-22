from fastapi import HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional
from hikayeapp_backend.models.story import Story
from hikayeapp_backend.models.user import User
from hikayeapp_backend.models.child import Child
from hikayeapp_backend.schemas.story import StoryRead, StoryCreate, StoryUpdate
from hikayeapp_backend.core.openai import StoryOpenAI


class StoryService:
    @staticmethod
    async def create_story(child_id:int, 
                     story_data: StoryCreate, 
                     session: Session,
                     current_user: User) -> StoryRead:
        
        _query_child = select(Child).where(Child.id==child_id)
        _child = session.exec(_query_child).first()

        # check child if exists
        if not _child:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                detail="Child not fround"
                                )
        
        if current_user.id != _child.user_id:
            raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
                                detail="You are not allowed to create a stroy for this child"
                                )

        story = Story(**story_data.dict(), child_id = child_id)

        _story_content = StoryOpenAI.create_story(prompt_from_human = story_data.prompt)
        
        story.story = _story_content
        session.add(story)
        session.commit()
        session.refresh(story)
        return StoryRead.from_orm(story)
    
    @staticmethod
    def get_story(story_id: int, session: Session) -> Optional[StoryRead]:
        story = session.get(Story, story_id)
        if story:
            return StoryRead.from_orm(story)
        return None

    @staticmethod
    def get_all_stories(session: Session) -> List[StoryRead]:
        stories = session.exec(select(Story)).all()
        return [StoryRead.from_orm(story) for story in stories]

    @staticmethod
    def update_story(story_id: int, story_data: StoryUpdate, session: Session) -> StoryRead:
        story = session.get(Story, story_id)
        if not Story:
            raise ValueError("Stroy not found")

        update_data = story_data.dict(exclude_unset = True)
        for key, value in update_data.items():
            setattr(story, key,value)

        session.add(story)
        session.commit()
        session.refresh(story)
        return StoryRead.from_orm(story)

    @staticmethod
    def delete_story(story_id: int, session: Session) -> bool:
        story = session.get(Story, story_id)
        if not story:
            raise ValueError("Story not found")
        session.delete(story)
        session.commit()
        return True



