from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import database,schemas,model,utils,auth2

router=APIRouter(
    tags=['Authentication']
)

# we write username instead of email
# password =password

@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user= db.query(model.User).filter(model.User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credential")

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    
    #create a token
    # return token

    access_token=auth2.create_access_token(data={"user_id":user.id})

    return {"access_token":access_token,"token_type":"bearer"}