from datetime import datetime

from uuid import UUID

from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic import EmailStr

from schemas.article_schema import ArticleSchema


class UserBaseSchema(BaseModel):
    user_uuid: Optional[UUID] = None
    user_name: str
    user_email: EmailStr
    is_admin: bool = False
    created_on: datetime
    updated_on: datetime
    
    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    user_password: str


class UserArticlesSchema(UserBaseSchema):
    articles: Optional[List[ArticleSchema]]


class UserUpdateSchema(UserBaseSchema):
    user_name: Optional[str]
    user_password: Optional[str]
    user_email: Optional[EmailStr]
    is_admin: Optional[bool]