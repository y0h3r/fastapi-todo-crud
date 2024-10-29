# app/services/base_service.py
from typing import Generic, TypeVar, List
from app.repositories.base import BaseRepository
from app.models.base import EntityMeta

T = TypeVar("T", bound=EntityMeta)  # type: ignore

class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    def create(self, entity: T) -> T:
        return self.repository.create(entity)
      
    def update(self, entity_id: int, updated_data: dict) -> T:
        return self.repository.update(entity_id, updated_data)
    
    def delete(self, entity_id: int) -> bool:
        return self.repository.delete(entity_id)
      
    def find_all(self) -> List[T]:
        return self.repository.find_all()

    def find_by_id(self, entity_id: int) -> T:
        return self.repository.find_by_id(entity_id)
