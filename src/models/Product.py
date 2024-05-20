from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: Optional[str] = None
    value: float
