from fastapi import Body

from schemas import product_schema as schemas


UpdateProductBody = Body(
    title='Product', 
    description='The product json representation.',
    examples=[
        schemas.UpdateProductSchema(
            id = 3, 
            name = 'Product 1', 
            value = 34.78
        )
    ]
)


CreateProductBody = Body(
    title='Product', 
    description='The product json representation.',
    examples=[
        schemas.CreateProductSchema(
            name = 'Product 1', 
            value = 33.78
        )
    ]
)

