from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"teste": "funfou!"}

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info" ,reload=True)