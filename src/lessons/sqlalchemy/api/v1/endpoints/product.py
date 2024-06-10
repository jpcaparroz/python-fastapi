from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from models.__all_models import ProductModel
from schemas.product_schema import ProductSchema
from core.deps import get_session
from data import crud
from data import template


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductModel)
async def post_product(product: ProductSchema,
                       db: AsyncSession = Depends(get_session)):
    new_product = ProductModel(name=product.name, value=product.value)

    return crud.create_product_query(product=new_product, db=db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ProductSchema])
async def get_products(db: AsyncSession = Depends(get_session)):
    return crud.get_products_query(db=db)


@router.get("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductSchema)
async def get_product(product_id: int, db: AsyncSession = Depends(get_session)):
    response = crud.get_product_query(product_id=product_id, db=db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    
    return response


@router.patch("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductSchema)
async def update_product(product_id: int, 
                         product_updated: ProductSchema = template.UpdatedProductBody, 
                         db: AsyncSession = Depends(get_session)):
    return crud.update_product_query(product_id=product_id, product_updated=product_updated, db=db)


@router.delete("/{product_id}", status_code=status.HTTP_204_OK, response_model=ProductSchema)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_session)):
    return crud.delete_product_query(product_id=product_id, db=db)