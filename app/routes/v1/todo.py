from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.get_db_session import get_db_session
from app.dependencies.get_user_from_request import get_user_from_request
from app.models.todo import Todo
from app.schemas.todo import TodoSchema, CreateTodoSchema, UpdateTodoSchema
from app.services.todo import TodoService


todo_router = APIRouter(prefix='/v1/todos', tags=['todos'])

@todo_router.get('/', response_model=List[TodoSchema])
async def find_all_todo(db: Session = Depends(get_db_session), user: str = Depends(get_user_from_request)):
    todo_service = TodoService(db)
    return todo_service.find_all(user_id=user['id'])

@todo_router.post('/', response_model=TodoSchema)
async def create_todo(todo: CreateTodoSchema, db: Session = Depends(get_db_session), user: str = Depends(get_user_from_request)):
  try:
    todo_service = TodoService(db)
    return todo_service.create(Todo(**dict(**todo.model_dump(), user_id=user['id'])))
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@todo_router.get('/{todo_id}', response_model=TodoSchema)
async def find_one_todo_by_id(todo_id: int, db: Session = Depends(get_db_session)):
  todo_service = TodoService(db)
  todo = todo_service.find_by_id(todo_id)
  if not todo:
      raise HTTPException(status_code=404, detail='Todo not found')
  return todo

@todo_router.put('/{todo_id}', response_model=TodoSchema)
async def update_todo(todo_id: int, todo: UpdateTodoSchema, db: Session = Depends(get_db_session), user: str = Depends(get_user_from_request)):
  todo_service = TodoService(db)
  updated_todo = todo_service.update(todo_id, Todo(**dict(**todo.model_dump(), user_id=user['id'])))
  if not updated_todo:
      raise HTTPException(status_code=404, detail='Todo not found')
  return updated_todo

@todo_router.delete('/{todo_id}', status_code=204)
async def delete_user(todo_id: int, db: Session = Depends(get_db_session)):
  todo_service = TodoService(db)
  if not todo_service.delete(todo_id):
      raise HTTPException(status_code=404, detail='Todo not found')