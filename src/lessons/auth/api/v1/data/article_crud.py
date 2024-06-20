from uuid import UUID

from typing import List

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.article_model import ArticleModel
from schemas import article_schema as schemas


# Article
async def create_article_query(article: ArticleModel, db: AsyncSession):
    async with db as session:
        session.add(article)
        await session.commit()
    
    return article


async def get_articles_query(db: AsyncSession):
    async with db as session:
        query = select(ArticleModel)
        result = await session.execute(query)
        articles: List[ArticleModel] = result.scalars().unique().all()
        
        return articles


async def get_article_query(article_uuid: UUID, db: AsyncSession):
    async with db as session:
        query = select(ArticleModel).filter(ArticleModel.article_uuid == article_uuid)
        result = await session.execute(query)
        article: ArticleModel = result.scalars().unique().one_or_none()

        return article


async def update_article_query(article_uuid: UUID, 
                               article_updated: schemas.ArticleSchema, 
                               db: AsyncSession):
    async with db as session:
        data = article_updated.model_dump(exclude_none=True, exclude_unset=True)
        query = update(ArticleModel).where(ArticleModel.article_uuid == article_uuid).values(data)
        await session.execute(query)
        await session.commit()
        
        response_query = select(ArticleModel).filter(ArticleModel.article_uuid == article_uuid)
        response = await session.execute(response_query)
        
        return response.scalars().unique().one_or_none()


async def delete_article_query(article_uuid: UUID, db: AsyncSession):
    async with db as session:
        query = delete(ArticleModel).where(ArticleModel.article_uuid == article_uuid)
        await session.execute(query)
        await session.commit()


# async def search_product_query(product_id: int, 
#                                db: AsyncSession):
#     async with db as session:
#         query = select(ProductModel).filter(ProductModel.id == product_id)
#         result = await session.execute(query)

#         return bool(result.scalar_one())

