from fastapi import FastAPI
from app.models.base import init_db

class ApplicationServer:
    def __init__(self) -> None:
      self.app = FastAPI()

    def get_server(self) -> FastAPI:
      init_db()
      return self.app