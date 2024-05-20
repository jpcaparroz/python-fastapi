from typing import List, Optional
from fastapi import FastAPI, HTTPException, status

from models import Product

app = FastAPI()

products = {
    1: {
        "id": 1,
        "name": "Test Product1",
        "value": 19.43
    },
    2: {
        "id": 2,
        "name": "Test Product2",
        "value": 11.42
    }
}

@app.get('/products')
async def get_products():
    return products

@app.get('/product/{product_id}')
async def get_product(product_id: int):
    try:
        product = products[product_id]
        return product
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Product ID not found.')
    
@app.post('/product', status_code=status.HTTP_201_CREATED)
async def post_product(product: Product):
    next_id: int = len(products) + 1
    products[next_id] = product
    return product

@app.put('/product/{product_id}')
async def put_product(product_id: int, product: Product):
    if product_id in products:
        products[product_id] = product
        return product
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Product ID= {product_id} non exists.')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", host ='localhost', port=8000, reload=True)
