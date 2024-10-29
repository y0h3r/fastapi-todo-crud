from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies.get_db_session import get_db_session
from app.models.user import User
from app.schemas.user import UserSchema, CreateUserSchema
from app.services.auth import AuthenticationService
from app.services.user import UserService


authentication_router = APIRouter(prefix='/auth', tags=['auth'])

@authentication_router.post('/sign-up', response_model=UserSchema)
async def create_user(user: CreateUserSchema, db: Session = Depends(get_db_session)):
  try:
    user_data = dict(
      name=user.name,
      email=user.email,
      hashed_password=user.password
    )
    user_service = UserService(db)
    return user_service.create(User(**user_data))
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))
  
@authentication_router.post('/login')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    print(authentication_router.routes)
    authentication_service = AuthenticationService(db)
    access_token = authentication_service.login(email=form_data.username, password=form_data.password)
    print(form_data)
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {'token': access_token}