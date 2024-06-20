from uuid import UUID

from typing import Optional

from pydantic import BaseModel


class ArticleSchema(BaseModel):
    article_uuid: Optional[UUID] = None
    title: str
    description: str
    source_url: str
    user: Optional[UUID]
    
    class Config:
        from_attributes = True