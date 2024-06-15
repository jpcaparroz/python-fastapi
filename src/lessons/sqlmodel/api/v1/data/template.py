from fastapi import Body
from fastapi import Query

from models.client_model import ClientModel


CreateClientBody = Body(
    title='Client', 
    description='The client json representation.',
    examples=[
        ClientModel(
            name='Rafaela',
            company='Roche'
        )
    ]
)


ClientIdQuery = Query(
    default=None,
    description='The client id',
    examples=[
        '3f333df6-90a4-4fda-8dd3-9485d27cee36',
        '6ecd8c99-4036-403d-bf84-cf8400f67836'
    ]
)

