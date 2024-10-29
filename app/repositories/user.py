from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.base import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, db_session: Session):
      super().__init__(User, db_session)
    
    def find_by_email(self, email: str) -> dict:
      user = self.db_session.query(self.model).filter(self.model.email == email).first()
      if user:
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "hashed_password": user.hashed_password
        }
      return None
