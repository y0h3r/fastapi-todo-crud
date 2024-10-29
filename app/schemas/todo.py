from pydantic import BaseModel
from typing import Optional

class TodoSchema(BaseModel):
    id: int
    content: str
    is_complete: bool
    user_id: int

class CreateTodoSchema(BaseModel):
    content: str
    is_complete: Optional[bool] = False

class UpdateTodoSchema(BaseModel):
    content: Optional[str] = None
    is_complete: Optional[bool] = None