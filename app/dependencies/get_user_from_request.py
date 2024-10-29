from fastapi import Request

async def get_user_from_request(request: Request):
  return request.state.user