from sqlalchemy.orm import Session
from typing import List
from app.models.todo import Todo
from app.repositories.base import BaseRepository

class TodoRepository(BaseRepository[Todo]):
    def __init__(self, db_session: Session):
        super().__init__(Todo, db_session)
    
    def find_all(self, user_id) -> List[Todo]:
        return self.db_session.query(self.model).filter(self.model.user_id == user_id).all()