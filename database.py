from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

conn_string = "postgresql://postgres:chetan@127.0.0.1:5432/chetan"
engine = create_engine(conn_string)

Session = sessionmaker(bind=engine)  # Prevent unexpected commits

Base = declarative_base()