from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

conn_string = "postgresql://postgres:chetan@127.0.0.1:5432/chetan"
engine = create_engine(conn_string)

Session=sessionmaker(bind=engine)

Base=declarative_base()