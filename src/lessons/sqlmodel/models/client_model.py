from uuid import uuid4
from uuid import UUID
from typing import Optional

from sqlmodel import SQLModel
from sqlmodel import Field


class ClientModel(SQLModel, table=True):
    __tablename__: str = 'client'
    
    id: Optional[UUID] = Field(primary_key=True, default_factory=uuid4, nullable=False)
    name: str = Field(default=None)
    company: Optional[str] = Field(default=None)