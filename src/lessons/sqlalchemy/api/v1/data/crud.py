from typing import List

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.__all_models import ProductModel
from schemas import product_schema as schemas


# Products
async def create_product_query(product: ProductModel, db: AsyncSession):
    db.add(product)
    await db.commit()
    
    return product


async def get_products_query(db: AsyncSession):
    async with db as session:
        query = select(ProductModel)
        result = await session.execute(query)
        products: List[ProductModel] = result.scalars().all()
        
        return products


async def get_product_query(product_id: int, db: AsyncSession):
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)

        return result.scalar_one()


async def update_product_query(product_id: int, 
                               product_updated: schemas.UpdateProductSchema, 
                               db: AsyncSession):
    async with db as session:
        data = product_updated.model_dump(exclude_none=True, exclude_unset=True)
        query = update(ProductModel).where(ProductModel.id == product_id).values(data)
        await session.execute(query)
        await session.commit()
        
        response_query = select(ProductModel).filter(ProductModel.id == product_id)
        response = await session.execute(response_query)
        
        return response.scalar_one()


async def delete_product_query(product_id: int, 
                               db: AsyncSession):
    async with db as session:
        query = delete(ProductModel).where(ProductModel.id == product_id)
        await session.execute(query)
        await session.commit()


async def search_product_query(product_id: int, 
                               db: AsyncSession):
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)

        return bool(result.scalar_one())

