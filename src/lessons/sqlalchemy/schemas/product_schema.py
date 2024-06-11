from typing import Optional

from pydantic import BaseModel


class BaseProductSchema(BaseModel):
    value: Optional[float] = None


class GetProductSchema(BaseModel):
    id: int
    name: str
    value: float


class CreateProductSchema(BaseProductSchema):
    name: str


class UpdateProductSchema(BaseProductSchema):
    id: Optional[int] = None
    name: Optional[str] = None

