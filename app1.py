from fastapi import FastAPI, Depends
from pydantic import BaseModel  
from model import User
from database import engine,Session,Base
import model
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

JWT_Secrets="markus"
Algorithm="HS256"

auth_scheme=OAuth2PasswordBearer(tokenUrl="token")

# is used to create database session object that interact with databases
session=Session()
model.Base.metadata.create_all(engine)

app=FastAPI()

users=session.query(User).all()

class Post(BaseModel):
    name:str
    age:int

@app.get("/sqlalchemy")
def read_data(token:Annotated[str,Depends(auth_scheme)]):
    return {"data":users[0].id , "token":token}

@app.post("/Insert_data")
def insert_data(data: Post):
    new_user = User(name=data.name, age=data.age)  # Removed 'id'
    session.add(new_user)
    session.commit()
    return {"data": "inserted"}


@app.put("/update_data/{id}")
def update(id:int,data:Post):
    user_data=session.query(User).filter(User.id==id).first()
    print(user_data)
    if user_data:
        user_data.name = data.name
        user_data.age = data.age
        session.commit()
        return {"data":"updated"}
    return {"data":"not found"}

@app.delete("/delete_data/{id}")
def delete(id:int):
    data=session.query(User).filter(User.id==id).first()
    if data:
        session.delete(data)
        session.commit()
        return {"data":"deleted"}
    return {"data":"not found"}

# user1=users[0]

# print(user1.name)

# User=user(id=1,name="Mohan",age=25)
# user2=user(id=2,name="Rohan",age=26)
# user3=user(id=3,name="Sohan",age=27)
# user4=user(id=4,name="Gohan",age=28)

# session.add_all([User,user2,user3,user4])

session.commit()