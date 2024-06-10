from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.__all_models import ProductModel


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