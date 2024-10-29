from sqlalchemy.ext.declarative import declarative_base
from app.config.database import DataBaseApplication

applicationDataBase = DataBaseApplication()
engine = applicationDataBase.get_engine()

EntityMeta = declarative_base()

def init_db():
  from app.models.user import User
  from app.models.todo import Todo
  EntityMeta.metadata.create_all(bind=engine)