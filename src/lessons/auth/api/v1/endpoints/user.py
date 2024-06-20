from uuid import UUID

from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.deps import get_session
from core.deps import get_current_user
from core.auth import authenticate
from core.auth import create_access_token
from core.security import generate_hash
from models.user_model import UserModel
from schemas import user_schema as schemas
from api.v1.data import user_crud as crud
from api.v1.data import user_template as template


router = APIRouter()


@router.get("/logged", status_code=status.HTTP_200_OK, response_model=schemas.GetUserSchema)
def get_logged_user(logged_user: UserModel = Depends(get_current_user)):
    return logged_user


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.GetUserSchema)
async def post_user(user: schemas.CreateUserSchema, db: AsyncSession = Depends(get_session)):
    new_user: UserModel = UserModel(
        user_name = user.user_name,
        user_email = user.user_email,
        user_password = generate_hash(user.user_password),
        is_admin = user.is_admin,
    )
    try:
        response = await crud.create_user_query(new_user, db)
        return response
    
    except IntegrityError:
        raise HTTPException(status.HTTP_409_CONFLICT, 'User with this email already registered')

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.GetUserSchema])
async def get_users(db: AsyncSession = Depends(get_session)):
    return await crud.get_users_query(db)


@router.get("/{user_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.GetUserSchema)
async def get_user(user_uuid: UUID, db: AsyncSession = Depends(get_session)):
    response = await crud.get_user_query(user_uuid, db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    return response


@router.patch("/{user_uuid}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.GetUserSchema)
async def update_user(user_uuid: UUID, user: schemas.UpdateUserSchema = template.UpdateUserBody, db: AsyncSession = Depends(get_session)):
    response = await crud.update_user_query(user_uuid, user, db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    return response 


@router.delete("/{user_uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(user_uuid: UUID, db: AsyncSession = Depends(get_session)):
    return await crud.delete_user_query(user_uuid, db)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='User info incorrect')
    
    return JSONResponse({"acess_token": create_access_token(user.user_uuid), "token_type": "bearer"})