from fastapi import APIRouter

from api.v1.endpoints import client


router = APIRouter()
router.include_router(client.router, prefix='/client', tags=['Client'])