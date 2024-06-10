from typing import Optional

from pydantic import BaseModel
from pydantic import field_validator

class Product(BaseModel):
    id: int
    name: Optional[str] = None
    value: float
    
    @field_validator('name')
    def validate_name(cls, value: str):
        # 1 Validation
        title = value.split(' ')
        if len(title) < 3:
            raise ValueError('The name must have 3 words.')
        
        # 2 Validation
        if value.islower():
            raise ValueError('The name must have capitalized.')
        
        return value
        

products = [
    Product(id=1, name='Product name 1', value=34.23),
    Product(id=2, name='Product name 2', value=35.23),
    Product(id=3, name='Product name 3', value=36.23)
]