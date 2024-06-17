from datetime import datetime

from uuid import UUID

from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic import EmailStr

from schemas.article_schema import ArticleSchema


class BaseUserSchema(BaseModel):
    user_name: str
    user_email: EmailStr
    is_admin: bool = False
    
    class Config:
        from_attributes = True


class CreateUserSchema(BaseUserSchema):
    user_password: str


class UserArticlesSchema(BaseUserSchema):
    articles: Optional[List[ArticleSchema]]


class UpdateUserSchema(BaseUserSchema):
    user_name: Optional[str]
    user_password: Optional[str]
    user_email: Optional[EmailStr]
    is_admin: Optional[bool]


class GetUserSchema(BaseUserSchema):
    user_uuid: Optional[UUID] = None
    created_on: Optional[datetime] = None
    updated_on: Optional[datetime] = None