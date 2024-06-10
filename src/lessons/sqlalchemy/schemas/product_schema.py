from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    value: Optional[float] = 0.0

