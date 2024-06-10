from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session


async def get_session():
    session: AsyncSession = Session()
    
    # open db connection and close after use
    try:
        yield session
    finally:
        await session.close()