from utils import Base, engine

from fastapi import FastAPI

app = FastAPI()
app.title = "Movies ApiRest"
app.version = "0.0.1"


Base.metadata.create_all(engine)
