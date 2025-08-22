import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from  hikayeapp_backend.utils.logger import get_logger

logger = get_logger("request")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000 # ms
        client_host = request.client.host if request.client else "unknown"
        
        user = getattr(request.state, "user", None)
        if user:
            user_str = f"user={user.id}, email={user.email}"
        else:
            user_str = "user=anonymous"
        
        logger.info(
                "%s %s - %s - %s - %d - %.2fms",
                request.method,
                request.url.path,
                client_host,
                user_str,
                response.status_code,
                process_time,
                )

        return response
