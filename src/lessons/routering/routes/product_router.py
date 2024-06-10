from fastapi import APIRouter


router = APIRouter()


@router.get("/api/v1/products")
async def get_products():
    return {"desc":"products"}