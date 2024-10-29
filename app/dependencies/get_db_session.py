from sqlalchemy.orm import Session
from app.config.database import DataBaseApplication

def get_db_session() -> Session:
    db = DataBaseApplication().get_configured_connection()
    try:
        yield db
    finally:
        db.close()