
from pydantic import BaseModel
from pydantic import Field

class MovieShema(BaseModel):
    title:str = Field(..., min_length=5, max_length=50)
    category:str = Field(..., min_length=5, max_length=50)
    year:int = Field(..., gt=1990)
    