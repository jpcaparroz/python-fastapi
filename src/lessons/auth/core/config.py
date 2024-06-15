from typing import ClassVar

from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import URL


class Settings(BaseSettings):
    """
    General configs
    """
    API_VERSION_ADDRESS: str = '/api/v1'
    DB_URL: URL = URL.create(drivername='postgresql+asyncpg',
                             username='postgres',
                             password='2509',
                             host='localhost',
                             port=5432,
                             database='postgres')
    DBBaseModel: ClassVar = declarative_base()
    
    JWT_SECRET: str = '60RVPSnYh0wgxd7PGqlNhaof3rvHqRv5GrKgqMkbmso'
    """
    generate random token
    
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    
    # 60 min * 24 hours * 7 days == 1 week
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        # important to follow
        case_sensitive = True


settings: Settings = Settings()