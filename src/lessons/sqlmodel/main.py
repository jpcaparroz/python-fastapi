from fastapi import FastAPI

from core.config import settings
from api.v1.api import router


app: FastAPI = FastAPI(title='SQLModel Example')
app.include_router(router, prefix=settings.API_VERSION_ADDRESS)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host='localhost', port=8000, log_level='info', reload=True)