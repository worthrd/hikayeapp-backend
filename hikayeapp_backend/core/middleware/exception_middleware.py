import traceback
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from hikayeapp_backend.utils.logger import get_logger

logger = get_logger("errors")


class ExceptionLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            user = getattr(request.state, "user", None)
            if user:
                user_str = f"user_id={user.id}, email={user.email}"
            else:
                user_str = "user=anonymous"

            logger.error(
                "Exception on %s %s - %s - %s\n%s",
                request.method,
                request.url.path,
                request.client.host if request.client else "unknown",
                user_str,
                "".join(traceback.format_exception(type(e), e, e.__traceback__)),
            )
            raise
