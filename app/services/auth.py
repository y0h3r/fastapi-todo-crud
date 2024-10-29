from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.repositories.user import UserRepository
from app.utils.encrypter import Encrypter
from app.config.enviroments import get_environment_variables
import jwt

class AuthenticationService():
    def __init__(self, db: Session):
      self.user_repository = UserRepository(db)
      self.encrypter = Encrypter()
        
    def get_user_by_email(self, email: str) -> dict:
      user = self.user_repository.find_by_email(email)
      if not user:
        return None
      return user
    
    def validate_password(self, user: dict, password: str) -> bool:
      return self.encrypter.validate_encrypted_text(password, user['hashed_password'])
    
    def login(self, email: str, password: str) -> str:
      user = self.get_user_by_email(email)
      if not user:
        return None
      
      if self.validate_password(user=user, password=password):
        token = self.create_access_token(user=user)
        return token
      return None
    
    def create_access_token(self, user: dict) -> str:
      ENV = get_environment_variables()
      to_encode = user.copy()
      utc_now = datetime.now(timezone.utc)
      expire = utc_now + timedelta(minutes=ENV.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
      to_encode.update({"exp": expire})
      encoded_jwt = jwt.encode(to_encode, ENV.JWT_SECRET_KEY, algorithm=ENV.JWT_ALGORITHM)
      return encoded_jwt