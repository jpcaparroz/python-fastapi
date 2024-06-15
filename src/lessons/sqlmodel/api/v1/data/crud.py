from typing import List

from pydantic import UUID4

from sqlalchemy.ext.asyncio import AsyncSession

from sqlmodel.sql.expression import select

from models.client_model import ClientModel


async def create_client_query(client: ClientModel, db: AsyncSession):
    db.add(client)
    await db.commit()
    
    return client


async def get_clients_query(db: AsyncSession):    
    async with db as session:
        query = select(ClientModel)
        result = await session.execute(query)
        clients: List[ClientModel] = result.scalars().all()
        
    return clients


async def get_client_query(client_id: UUID4,
                           db: AsyncSession):    
    async with db as session:
        query = select(ClientModel).filter(ClientModel.id == client_id)
        result = await session.execute(query)
        client: ClientModel = result.scalar_one_or_none()
        
    return client
