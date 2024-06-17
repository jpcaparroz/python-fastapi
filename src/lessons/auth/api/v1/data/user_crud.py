from uuid import UUID

from typing import List

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_model import UserModel
from schemas import user_schema as schemas
from core.security import generate_hash


# User
async def create_user_query(user: UserModel, db: AsyncSession):
    async with db as session:
        session.add(user)
        await session.commit()
    
    return user


async def get_users_query(db: AsyncSession):
    async with db as session:
        query = select(UserModel)
        result = await session.execute(query)
        users: List[UserModel] = result.scalars().unique().all()
        
    return users


async def get_user_query(user_uuid: UUID, db: AsyncSession):
    async with db as session:
        query = select(UserModel).filter(UserModel.user_uuid == user_uuid)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()
        
    return user


async def update_user_query(user_uuid: UUID, updated_user: schemas.UpdateUserSchema, db: AsyncSession):
    async with db as session:
        data = updated_user.model_dump(exclude_none=True, exclude_unset=True)
        if data.get('user_password'):
            data['user_password'] = generate_hash(updated_user.user_password)
        
        query = update(UserModel).where(UserModel.user_uuid == user_uuid).values(data)
        await session.execute(query)
        await session.commit()
        
        response_query = select(UserModel).filter(UserModel.user_uuid == user_uuid)
        response = await session.execute(response_query)
        
        return response.scalars().unique().one_or_none()


async def delete_user_query(user_uuid: UUID, db: AsyncSession):
    async with db as session:
        query = delete(UserModel).where(UserModel.user_uuid == user_uuid)
        await session.execute(query)
        await session.commit()