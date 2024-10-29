from sqlalchemy.orm import Session
from typing import Generic, Type, TypeVar, List
from app.models.base import EntityMeta

T = TypeVar("T", bound=EntityMeta)  # type: ignore

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], db_session: Session):
        self.model = model
        self.db_session = db_session
        
    def create(self, entity: T) -> T:
        self.db_session.add(entity)
        self.db_session.commit()
        self.db_session.refresh(entity)
        return entity

    def update(self, entity_id: int, updated_data: dict) -> T:
        entity = self.find_by_id(entity_id)
        if entity:
            for key, value in updated_data.items():
                setattr(entity, key, value)
            self.db_session.commit()
            self.db_session.refresh(entity)
            return entity
        return None
      
    def delete(self, entity_id: int) -> bool:
        entity = self.find_by_id(entity_id)
        if entity:
            self.db_session.delete(entity)
            self.db_session.commit()
            return True
        return False
      
    def find_all(self) -> List[T]:
        return self.db_session.query(self.model).all()

    def find_by_id(self, entity_id: int) -> T:
        return self.db_session.query(self.model).filter(self.model.id == entity_id).first()
