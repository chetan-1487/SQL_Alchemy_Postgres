from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from pydantic import BaseModel  
from model import engine,User
from model import Base

app=FastAPI()
# is used to create database session object that interact with databases
Session=sessionmaker(bind=engine)
session=Session()
Base.metadata.create_all(engine)

users=session.query(User).all()

class post(BaseModel):
    id:int
    name:str
    age:int

@app.get("/sqlalchemy")
def read_data():
    return {"data":users[0].id}

@app.post("/Insert_data")
def insert_data(data:post):
    new_user=User(id=data.id,name=data.name,age=data.age)
    session.add(new_user)
    session.commit()
    return {"data":"inserted"}

@app.put("/update_data/{id}")
def update(id:int,data:post):
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