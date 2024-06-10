from fastapi import FastAPI

from routes import user
from routes import product


app = FastAPI()
app.include_router(product, tags=['products'])
app.include_router(user, tags=['users'])


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app="main:app", host ='localhost', port=8000, reload=True)