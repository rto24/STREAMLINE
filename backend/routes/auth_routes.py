from fastapi import APIRouter, HTTPException, Query
from backend.controllers.auth_controller import generate_spotify_login_url, handle_spotify_callback
from fastapi.responses import RedirectResponse
from fastapi import Response

router = APIRouter()

@router.get("/login")
async def login():
  auth_url = await generate_spotify_login_url()
  return {"auth_url": auth_url}

@router.get("/callback")
async def callback(code: str):
  try:
    data = await handle_spotify_callback(code)
    jwt_token = data["jwt_token"]
    
    frontend_url = "http://localhost:3000/home"
    response = RedirectResponse(url=f"{frontend_url}")
    response.set_cookie(
      key="spotify_jwt",
      value=jwt_token,
      httponly=True,
      secure=False,
      samesite="Strict",
      max_age = 60*60
    )
    return response
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))