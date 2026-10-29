from fastapi import APIRouter, HTTPException
from schemas.schemas import LoginRequest
from models.users_models import get_user_from_email
from utils.utils import verify_password, create_access_token


auth_router = APIRouter(prefix="/auth")

@auth_router.post("/login")
def login(body: LoginRequest):

    if body.email == "" or body.email is None:
        raise HTTPException(
            status_code= 400
            , detail= {"code": "MISSING_INPUT", "message": "Please enter email"}
        )

    if body.password == "" or body.password is None:
            raise HTTPException(
                status_code= 400
                , detail= {"code": "MISSING_INPUT", "message": "Please enter password"}
            )
    
    user = get_user_from_email(body.email)

    if user is None:
         raise HTTPException(
              status_code=401
              , detail= {"code": "UNAUTHORISED", "message": "Email or password is incorrect"}
         )

    if verify_password(body.password, user["password_hash"]):
        return {
            "access_token": create_access_token(user["id"])
            , "token_type": "bearer"
        }
    else:
         raise HTTPException(
              status_code=401
              , detail= {"code": "UNAUTHORISED", "message": "Email or password is incorrect"}
         )


    
