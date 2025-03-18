from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# class Post(BaseModel):
#     title:str
#     content:str
#     published:bool=True # for default value if we dont not pass value of published

# class CreatePost(BaseModel):
#     title:str
#     content:str
#     published:bool=True

# class UpdatePost(BaseModel):
#     title:str
#     content:str
#     published:bool

class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True

class PostCreate(PostBase):
    pass

#post response class
class Post(PostBase):
    id:int
    created_At:datetime

    class config:
        orm_mode=True

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_At:datetime

    class config:
        orm_mode=True

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id:Optional[str]=None