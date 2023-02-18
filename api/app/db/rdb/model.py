from uuid import uuid4

from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from app.db.rdb.base import Base


class Exgauster(Base):
    __tablename__ = 'exgauster'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String())


class Component(Base):
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(256))
    exgauster_uuid = Column(UUID(as_uuid=True), ForeignKey('exgauster.uuid'))


class BearingBig(Component):
    __tablename__ = 'bearing_big'

    exgauster = relationship('Exgauster', backref='bearings_big')
