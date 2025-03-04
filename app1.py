from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from model import User
from database import engine, Session as SessionLocal, Base
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
import schemas

JWT_SECRET = "markus"
ALGORITHM = "HS256"

auth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create tables if they don't exist
Base.metadata.create_all(engine)

app = FastAPI()

# Dependency injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/sqlalchemy")
def read_data(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return {"data": users[0].id}

@app.post("/Insert_data")
def insert_data(data: schemas.Post, db: Session = Depends(get_db)):
    new_user = User(name=data.name, age=data.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"data": f"User {new_user.id} inserted"}

@app.put("/update_data/{id}")
def update(id: int, data: schemas.Update_Post, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    # Ensure we are modifying an instance of User
    setattr(user_data, "name", data.name)
    setattr(user_data, "age", data.age)

    db.commit()
    db.refresh(user_data)  # Refresh to update session state

    return {"data": "updated"}



@app.delete("/delete_data/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == id).first()
    if user_data:
        db.delete(user_data)
        db.commit()
        return {"data": "deleted"}
    raise HTTPException(status_code=404, detail="User not found")
