from pydantic_settings import BaseSettings

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
                             database='sqlmodel')
    
    class Config:
        # important to follow
        case_sensitive = True


settings: Settings = Settings()