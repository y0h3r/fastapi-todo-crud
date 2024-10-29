from typing import List
from sqlalchemy.orm import Session
from app.repositories.todo import TodoRepository
from app.models.todo import Todo
from app.services.base import BaseService
        
class TodoService(BaseService[Todo]):
  def __init__(self, db: Session):
    repository = TodoRepository(db)
    super().__init__(repository)
  
  def find_all(self, user_id: str) -> List[Todo]:
    return self.repository.find_all(user_id)