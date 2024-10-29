from fastapi import Depends
from sqlalchemy.orm import Session
from app.repositories.user import UserRepository
from app.models.user import User
from app.services.base import BaseService
from app.config.database import get_db_session
from app.utils.encrypter import Encrypter

class UserService(BaseService[User]):
    def __init__(self, db: Session = Depends(get_db_session)):
        repository = UserRepository(db)
        self.encrypter = Encrypter()
        super().__init__(repository)
        
    def create(self, entity):
      entity.hashed_password = self.encrypter.encrypt(entity.hashed_password)
      return super().create(entity)