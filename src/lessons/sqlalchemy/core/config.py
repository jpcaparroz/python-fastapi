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
    
    class Config:
        # important to follow
        case_sensitive = True


settings = Settings()