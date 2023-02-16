from uuid import uuid4

from sqlalchemy import Column, String, UUID

from .base import Base


class User(Base):
    __tablename__ = 'user'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(), index=True)
    email = Column(String(256), unique=True)
    hashed_password = Column(String)




