
from utils import JwtManager

from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status

class JwtBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = JwtManager.validate_token( auth.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="Invalid Credentials"
            )