from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
conn=os.getenv("connection")

if not conn:
    raise ValueError("Database connection string is missing. Please check your .env file.")

engine=create_engine(conn)

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()