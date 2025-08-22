from fastapi import FastAPI
from hikayeapp_backend.database import init_db
from hikayeapp_backend.api.v1  import routes_auth, routes_users
from hikayeapp_backend.core.routes.child import router as child_router
from hikayeapp_backend.core.routes.story import router as story_router

from hikayeapp_backend.core.middleware.logging_middleware import LoggingMiddleware
from hikayeapp_backend.core.middleware.exception_middleware import ExceptionLoggingMiddleware

app = FastAPI(title = "HikayeApp Backend", version = "1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

app.add_middleware(LoggingMiddleware)    
app.add_middleware(ExceptionLoggingMiddleware)    

app.include_router(story_router, prefix="/api/v1")
app.include_router(child_router, prefix="/api/v1")
app.include_router(routes_auth.router, prefix="/api/v1")
app.include_router(routes_users.router, prefix="/api/v1")

