from config import Base, engine
from routers import movie_router, user_router
from middlewares import ErrorHandler

from fastapi import FastAPI

app = FastAPI()
app.title = "Movies ApiRest"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(engine)
