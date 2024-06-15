from typing import AsyncGenerator

from sqlmodel.ext.asyncio.session import AsyncSession

from core.database import Session


async def get_session() -> AsyncGenerator:
    session : AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()