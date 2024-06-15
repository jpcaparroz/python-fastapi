from pytz import timezone

from typing import Optional
from typing import List

from pydantic import EmailStr

from datetime import datetime
from datetime import timedelta

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from models.user_model import UserModel
from core.config import settings
from core.security import verify_password


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_VERSION_ADDRESS}/user/login'
    
)


async def authenticate(email: EmailStr, password: str, db: AsyncSession) -> Optional[UserModel]:
    async with db as session:
        query = select(UserModel).filter(UserModel.email == email)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()
        
        if not user:
            return None
        
        if not verify_password(password, user.password):
            return None

    return user


def _create_token(token_type: str, lifetime: timedelta, subject: str) -> str:
    # Infos: https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    payload = {}
    time_zone = timezone('America/Sao_Paulo')
    expire = datetime.now(tz=time_zone) + lifetime
    
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.now(tz=time_zone) # issued at
    payload["sub"] = str(subject)
    
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

