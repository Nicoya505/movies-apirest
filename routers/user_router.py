from shemas import UserShema
from utils import JwtManager

from fastapi import APIRouter
from fastapi import status,Body
from fastapi.responses import JSONResponse

user_router = APIRouter()

@user_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    tags=["Auth"]
)
def login(user: UserShema = Body(...)):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = JwtManager.create_token(user.model_dump())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
    
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "user not found"})