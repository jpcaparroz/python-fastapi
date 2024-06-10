from fastapi import Body

from schemas import product_schema


UpdatedProductBody = Body(
    title='Product', 
    description='The client json representation.',
    examples=[
        product_schema.ProductSchema(
            id = 3, 
            name = 'Product 1', 
            value = 34.78
        )
    ]
)

