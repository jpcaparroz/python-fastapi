from typing import AsyncGenerator
from typing import Optional

from fastapi import HTTPException
from fastapi import Depends
from fastapi import status

from jose import jwt
from jose import JWTError

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from pydantic import BaseModel

from core.database import Session
from core.auth import oauth2_schema
from core.config import settings
from models.user_model import UserModel


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()


async def get_current_user(db: AsyncSession = Depends(get_session), 
                           token: str = Depends(oauth2_schema)) -> UserModel:
    credential_exception: HTTPException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                                        detail="Authorization failed",
                                                        headers={"WWW-Authenticate": "Bearer"})
    
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            [settings.ALGORITHM],
            {"verify_aud": False}
        )
        
        username: str = payload.get("sub")
        if not username:
            raise credential_exception
        
        token_data: TokenData = TokenData(username=username)

    except JWTError:
        raise credential_exception
    
    async with db as session:
        query = select(UserModel).filter(UserModel.user_uuid == token_data.username)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()
        
        if not user:
            raise credential_exception
        
        return user
                