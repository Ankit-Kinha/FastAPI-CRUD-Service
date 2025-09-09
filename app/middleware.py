from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import os

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # allow docs and health without API key
        if request.url.path.startswith('/docs') or request.url.path.startswith('/openapi.json') or request.url.path == '/health':
            return await call_next(request)

        expected = os.getenv("SECRET_API_KEY")
        if not expected:
            return await call_next(request)

        api_key = request.headers.get("x-api-key") or request.query_params.get("api_key")
        if api_key != expected:
            raise HTTPException(status_code=401, detail="Invalid or missing API Key")
        return await call_next(request)
