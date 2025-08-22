from typing import List, Optional
from sqlmodel import Session, select
from hikayeapp_backend.models.child import Child
from hikayeapp_backend.models.user import User
from hikayeapp_backend.schemas.child import ChildCreate, ChildUpdate


class ChildService:
    @staticmethod
    def create_child(session: Session, child_in: ChildCreate, current_user: User) -> Child:
        child = Child(**child_in.dict(), user_id = current_user.id)
        session.add(child)
        session.commit()
        session.refresh(child)
        return child
    
    @staticmethod
    def get_child(session: Session, child_id: int) -> Child:
        return session.get(Child, child_id)

    @staticmethod
    def list_childeren(session: Session, current_user: User) -> List[Child]:
        query = select(Child).where(Child.user_id == current_user.id)
        return session.exec(query).all()

    @staticmethod
    def update_child(session: Session, child_id: int, child_in: ChildUpdate) -> Optional[Child]:
        child = session.get(Child, child_id)
        if not child:
            return None
        for key, value in child_in.dict(exclude_unset = True).items():
            setattr(child, key, value)
        session.add(child)
        session.commit()
        session.refresh(child)
        return child
    
    @staticmethod
    def delete_child(session: Session, child_id: int) -> bool:
        child = session.get(Child, child_id)
        if not Child:
            return False
        session.delete(child)
        session.commit()
        return True




        






