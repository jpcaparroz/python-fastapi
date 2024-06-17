from uuid import UUID
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import UUID
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'user'
    
    user_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_name = Column(String(256), nullable=True)
    user_email = Column(String(256), index=True, nullable=False, unique=True)
    user_password = Column(String(256), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
    article = relationship("ArticleModel", cascade="all,delete-orphan", back_populates="creator", uselist=True, lazy="joined")