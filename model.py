from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from database import Base  # Ensure Base is correctly imported from database.py

class User(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
