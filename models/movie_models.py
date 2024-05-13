from config import Base

from datetime import datetime

from sqlalchemy import Column,Integer, String,DateTime

class MovieModel(Base):
    __tablename__= "movieModels"
    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    year = Column(Integer(), nullable=False)
    created_at = Column(DateTime(),default=datetime.now())