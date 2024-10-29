from pydantic import BaseModel

class UserSchema(BaseModel):
  id: int
  name: str
  email: str
  hashed_password: str

class CreateUserSchema(BaseModel):
  name: str
  email: str
  password: str
    
class UpdateUserSchema(BaseModel):
  id: int
  name: str
  email: str
  password: str
  