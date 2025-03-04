from pydantic import BaseModel

class Post(BaseModel):
    name: str
    age: int

class Create_Post(Post):  # Inherit to avoid redundancy
    id: int

class Update_Post(Post):  # Inherit from Post
    pass
