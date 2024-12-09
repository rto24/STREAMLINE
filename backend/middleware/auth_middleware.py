from fastapi import Request, HTTPException
from jose import jwt, JWTError
from backend.config import JWT_SECRET, JWT_ALGORITHM

async def jwt_middleware_config(request: Request):
  token = request.cookies.get("spotify_jwt")
  
  if not token and "Authorization" in request.headers:
    auth_header = request.headers["Authorization"]
    if auth_header.startswith("Bearer "):
      token = auth_header.split(" ")[1]
      
  if not token:
    raise HTTPException(status_code=401, detail="Missing JWT token")
  
  try:
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    print("PAYLOAD FROM MIDDLEWARE", payload)
    return payload
  except JWTError as e:
    raise HTTPException(status_code=401, detail="Invalid token")
  
async def jwt_middleware_access_token(request: Request):
  token = request.cookies.get("spotify_jwt")
  if not token:
    raise HTTPException(status_code=401, detail="Missing JWT token")
  try: 
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload["spotify_access_token"]
  except JWTError as e:
    raise HTTPException(status_code=401, detail="Invalid token")