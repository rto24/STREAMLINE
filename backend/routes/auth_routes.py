from fastapi import APIRouter, HTTPException
from backend.controllers.auth_controller import generate_spotify_login_url, handle_spotify_callback

router = APIRouter()

@router.get("/login")
async def login():
  auth_url = await generate_spotify_login_url()
  return {"auth_url": auth_url}

@router.get("/callback")
async def callback(code: str):
  try:
    tokens = await handle_spotify_callback(code)
    return {"message": "User authenticated", "tokens": tokens}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))