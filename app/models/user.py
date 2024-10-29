from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import EntityMeta

class User(EntityMeta):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    
    todos = relationship("Todo", back_populates="user", cascade="all, delete-orphan")
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}