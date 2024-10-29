from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from app.config.enviroments import get_environment_variables

ENV = get_environment_variables()

class DataBaseApplication:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataBaseApplication, cls).__new__(cls)
            cls._instance.init_app()
        return cls._instance

    def init_app(self):
        self.SQLALCHEMY_DATABASE_URI = ENV.DB_URI.format(ENV.DB_USR, ENV.DB_PWD)
        self.engine = self.get_engine()
        self.session_factory = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Session = scoped_session(self.session_factory)

    def get_engine(self) -> Engine:
        return create_engine(self.SQLALCHEMY_DATABASE_URI, echo=True, future=True)

    def get_configured_connection(self) -> Session:
        return self.Session()

def get_db_session() -> Session:
    db = DataBaseApplication().get_configured_connection()
    try:
        yield db
    finally:
        db.close()