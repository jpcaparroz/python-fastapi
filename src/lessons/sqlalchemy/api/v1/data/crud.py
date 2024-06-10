from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.__all_models import ProductModel
from schemas.product_schema import ProductSchema


# Products
async def create_product_query(product: ProductModel, db: AsyncSession):
    db.add(product)
    await db.commit()
    
    return product


async def get_products_query(db: AsyncSession):
    async with db as session:
        query = select(ProductModel)
        result = await session.execute(query)
        
        return result.all()


async def get_product_query(product_id: int, db: AsyncSession):
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)

        return result.scalar_one()


async def update_product_query(product_id: int, 
                               product_updated: ProductSchema, 
                               db: AsyncSession):
    async with db as session:
        data = product_updated.model_dump(exclude_none=True, exclude_unset=True)
        
        query = update(ProductModel).where(ProductModel.id == product_id).values(data)
        result = await session.execute(query)
        return result.scalar_one()


async def update_product_query(product_id: int, 
                               db: AsyncSession):
    async with db as session:
        query = delete(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)
        db.commit()

        return result