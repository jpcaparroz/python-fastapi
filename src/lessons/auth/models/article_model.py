from uuid import UUID
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from core.config import settings


class ArticleModel(settings.DBBaseModel):
    __tablename__ = 'article'
    
    article_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(256))
    description = Column(String(256))
    source_url = Column(String(256))
    user = Column(UUID(as_uuid=True), ForeignKey('user.user_uuid'))
    creator = relationship("UserModel", back_populates='article', lazy='joined')