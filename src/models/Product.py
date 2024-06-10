from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: Optional[str] = None
    value: float


products = [
    Product(id=1, name='Product1', value=34.23),
    Product(id=2, name='Product2', value=35.23),
    Product(id=3, name='Product3', value=36.23)
]