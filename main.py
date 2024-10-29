from app.config.server import ApplicationServer
from app.middlewares.jwt import JWTMiddleware
from app.routes.v1.todo import todo_router
from app.routes.v1.auth import authentication_router
from dotenv import load_dotenv

load_dotenv()
app = ApplicationServer()
server = app.get_server()

server.add_middleware(JWTMiddleware)
server.include_router(todo_router, prefix='/api')
server.include_router(authentication_router, prefix='/api')