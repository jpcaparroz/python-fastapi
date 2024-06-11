from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from models.__all_models import ProductModel
from schemas import product_schema as schemas
from core.deps import get_session
from api.v1.data import crud
from api.v1.data import template


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.GetProductSchema)
async def post_product(product: schemas.CreateProductSchema = template.CreateProductBody,
                       db: AsyncSession = Depends(get_session)):
    new_product = ProductModel(name=product.name, value=product.value)

    return await crud.create_product_query(product=new_product, db=db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.GetProductSchema])
async def get_products(db: AsyncSession = Depends(get_session)):
    return await crud.get_products_query(db=db)


@router.get("/{product_id}", status_code=status.HTTP_200_OK, response_model=schemas.GetProductSchema)
async def get_product(product_id: int, db: AsyncSession = Depends(get_session)):
    response = await crud.get_product_query(product_id=product_id, db=db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    
    return response


@router.patch("/{product_id}", status_code=status.HTTP_200_OK, response_model=schemas.GetProductSchema)
async def update_product(product_id: int, 
                         product_updated: schemas.UpdateProductSchema = template.UpdateProductBody, 
                         db: AsyncSession = Depends(get_session)):
    return await crud.update_product_query(product_id=product_id, product_updated=product_updated, db=db)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_session)):
    return await crud.delete_product_query(product_id=product_id, db=db)


async def search_product(product_id: int, db: AsyncSession = Depends(get_session)):
    response = await crud.search_product_query(product_id=product_id, db=db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    
    return response

