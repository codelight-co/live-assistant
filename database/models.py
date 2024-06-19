import uuid

from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from schemas.models import UserRole
from database.connection import Base, engine


class Posts(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String)
    description = Column(String)

class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    role = Column(Enum(UserRole))

class Companies(Base):
    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String)
    agent_id = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("Users")


Base.metadata.create_all(engine)
