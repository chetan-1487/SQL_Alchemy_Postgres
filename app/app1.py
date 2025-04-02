from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import model, schemas, utils
from .database import engine
from .router import post, user, auth

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"Favorite","content":"I like pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i
    

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/",description="This is my first route") #we can fast description in fastapi port
def root():
    return {"Message":"Successfully Running FastAPI"}

# @app.post("/create")
# def create_post(payload:dict=Body(...)):
#     print(payload)
#     return {"message":"Successfully created"}