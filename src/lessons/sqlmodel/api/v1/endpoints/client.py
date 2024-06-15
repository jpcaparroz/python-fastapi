from typing import List

from pydantic import UUID4

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from models.client_model import ClientModel
from core.deps import get_session
from api.v1.data import crud
from api.v1.data import template


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClientModel)
async def post_client(client: ClientModel = template.CreateClientBody,
                      db: AsyncSession = Depends(get_session)):
    response = await crud.create_client_query(client, db)
    return response


@router.get("/all/", status_code=status.HTTP_200_OK, response_model=List[ClientModel])
async def get_clients(db: AsyncSession = Depends(get_session)):
    response = await crud.get_clients_query(db)
    return response


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ClientModel])
async def get_client(client_id: UUID4 = template.ClientIdQuery,
                      db: AsyncSession = Depends(get_session)):
    response = await crud.get_client_query(client_id, db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Client not found')
    return response