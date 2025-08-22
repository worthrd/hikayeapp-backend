from sqlmodel import SQLModel, create_engine, Session
from hikayeapp_backend.config import settings

engine = create_engine(settings.DATABASE_URL, echo = True)

def get_session():

    with Session(engine) as session: 
        yield session


def init_db():

    from hikayeapp_backend.models.user import User
    from hikayeapp_backend.models.story import Story

    SQLModel.metadata.create_all(engine)


def drop_db():
    
    from hikayeapp_backend.models.user import User
    from hikayeapp_backend.models.story import Story

    SQLModel.metadata.drop_all(engine)
