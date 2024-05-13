import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

database_name = "../database.sqlite"
database_dir = os.path.dirname( os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(database_dir, database_name)}"

engine = create_engine(database_url)

session = sessionmaker(engine)

Base = declarative_base()