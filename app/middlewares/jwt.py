import jwt
from fastapi import Request, status
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse
from app.config.enviroments import get_environment_variables

ENV = get_environment_variables()
class JWTMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
    prefix = '/api/v1'

    if request.url.path.startswith(prefix):
      token = request.headers.get('Authorization')

      if not token or not token.startswith('Bearer '):
        return JSONResponse(
          status_code=status.HTTP_401_UNAUTHORIZED,
          content={
            'detail': 'Authorization header missing or invalid format',
            'status': status.HTTP_401_UNAUTHORIZED
          }
        )
      token = token.split(' ')[1]
      try:
        request.state.user = self.decodeToken(token)
      except jwt.ExpiredSignatureError:
        return JSONResponse(
          status_code=status.HTTP_401_UNAUTHORIZED,
          content={
            'detail': 'Token expired',
            'status': status.HTTP_401_UNAUTHORIZED
          }
        )
      except jwt.InvalidTokenError:
        return JSONResponse(
          status_code=status.HTTP_401_UNAUTHORIZED,
          content={
            'detail': 'Invalid token',
            'status': status.HTTP_401_UNAUTHORIZED
          }
        )
    return await call_next(request)

  def decodeToken(self, token: str) -> dict:
    return jwt.decode(token, ENV.JWT_SECRET_KEY, algorithms=[ENV.JWT_ALGORITHM])
