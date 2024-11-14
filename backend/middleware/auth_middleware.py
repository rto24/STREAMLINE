from fastapi import Request, HTTPException
from jose import jwt, JWTError
from backend.config import JWT_SECRET, JWT_ALGORITHM

async def jwt_middleware_config(request: Request):
  token = request.cookies.get("spotify_jwt")
  if not token:
    raise HTTPException(status_code=401, detail="Missing JWT token")
  try:
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload
  except JWTError as e:
    raise HTTPException(status_code=401, detail="Invalid token")