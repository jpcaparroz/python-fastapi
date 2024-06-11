from fastapi import FastAPI

from core.config import settings
from api.v1.api import api_router


app = FastAPI(title='FastAPI do Zero')

app.include_router(api_router, prefix=settings.API_VERSION_ADDRESS)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host='localhost', port=8000, log_level='info', reload=True)