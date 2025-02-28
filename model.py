from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import declarative_base

conn_string = "postgresql://postgres:chetan@127.0.0.1:5432/chetan"

engine = create_engine(conn_string)

Base=declarative_base()

class user(Base):
    __tablename__="client"

    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

Base.metadata.create_all(engine)