from pydantic import BaseModel

class UserShema(BaseModel):
    email: str
    password: str