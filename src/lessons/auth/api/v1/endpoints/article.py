from uuid import UUID

from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.deps import get_current_user
from models.__all_models import ArticleModel
from models.__all_models import UserModel
from schemas import article_schema as schemas
from schemas import user_schema
from api.v1.data import article_crud as crud
from api.v1.data import article_template as template


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ArticleSchema)
async def post_article(article: schemas.ArticleSchema = template.CreateArticleBody,
                       logged_user: UserModel = Depends(get_current_user),
                       db: AsyncSession = Depends(get_session)):
    new_article: ArticleModel = ArticleModel(**article.model_dump())

    return await crud.create_article_query(article=new_article, db=db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ArticleSchema])
async def get_articles(db: AsyncSession = Depends(get_session)):
    return await crud.get_articles_query(db=db)


@router.get("/{article_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.ArticleSchema)
async def get_article(article_uuid: UUID, db: AsyncSession = Depends(get_session)):
    response = await crud.get_article_query(article_uuid=article_uuid, db=db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')

    return response


@router.patch("/{article_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.ArticleSchema)
async def update_article(article_uuid: UUID, 
                         article_updated: schemas.ArticleSchema = template.UpdateArticleBody, 
                         db: AsyncSession = Depends(get_session)):
    response = await crud.update_article_query(article_uuid=article_uuid, article_updated=article_updated, db=db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')

    return response 


@router.delete("/{article_uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_uuid: UUID, db: AsyncSession = Depends(get_session)):
    response = await crud.delete_article_query(article_uuid=article_uuid, db=db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')

    return response 

