from fastapi import APIRouter

from api.v1.endpoints import article
from api.v1.endpoints import user


router = APIRouter()
router.include_router(article.router, prefix='/article', tags=['Article'])
router.include_router(user.router, prefix='/user', tags=['User'])