from uuid import UUID

from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl


class ArticleSchema(BaseModel):
    article_uuid: Optional[UUID] = None
    title: str
    description: str
    source_url: HttpUrl
    user: Optional[UUID]
    
    class Config:
        from_attributes = True