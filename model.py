from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import declarative_base
from database import Base


class User(Base):
    __tablename__="client"

    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)

