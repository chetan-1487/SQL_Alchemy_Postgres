from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import model, schemas, utils, auth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router=APIRouter(
    prefix="/posts",
    tags=['posts']
)

@router.get("/",response_model=List[schemas.Post])
def get_post(db:Session=Depends(get_db)):
    posts=db.query(model.Post).all()
    return posts

# @router.get("/posts/latest")
# def get_latest_post():
#     post=my_posts[len(my_posts)-1]
#     return {"detail":post}

@router.get("/{id}",response_model=schemas.Post)
def get_post_id(id:int,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):
    # post=find_post(id)

    curr_post=db.query(model.Post).filter(model.Post.id==id).first()
    print(curr_post)

    if not curr_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id: {id} not found"}
    return curr_post

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post:schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):

    new_post=model.Post(**post.model_dump(),user_id=current_user.id)
    # new_post=model.Post(title=post.title,content=post.content,published=post.published)
    # post_dict=post.model_dump() # model_dump is used instead of dict
    # post_dict["id"]=randrange(0,1000000)
    # my_posts.append(post_dict)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):
    # index=find_index_post(id)
    # post_dict=post.model_dump()
    # post_dict['id']=id
    # my_posts[index]=post_dict
    post_query=db.query(model.Post).filter(model.Post.id==id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} not found")
    
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):
    # index=find_index_post(id)
    post=db.query(model.Post).filter(model.Post.id==id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
