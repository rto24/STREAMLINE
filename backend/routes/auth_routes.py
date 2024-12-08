from fastapi import APIRouter, HTTPException, Query, Response, Depends, Request
from backend.controllers.auth_controller import generate_spotify_login_url, handle_spotify_callback
from backend.middleware.auth_middleware import jwt_middleware_config
from backend.db.supabase_client import get_user_by_username, insert_user
from fastapi.responses import RedirectResponse


router = APIRouter()

@router.get("/login")
async def login():
  auth_url = await generate_spotify_login_url()
  return {"auth_url": auth_url}

@router.get("/callback")
async def callback(code: str):
  try:
    data = await handle_spotify_callback(code)

    if not data or "profile_data" not in data or "jwt_token" not in data:
        raise ValueError(f"Invalid data returned from handle_spotify_callback: {data}")

    username = data["profile_data"]["id"]
    jwt_token = data["jwt_token"]

    if not username:
        raise ValueError(f"Username not found in profile data: {data}")

    print(f"Username: {username}, JWT: {jwt_token}")
    playlists = []

    existing_user = get_user_by_username(username)
    print("Existing user response:", existing_user)

    if not existing_user:
      insert_user(username, playlists)
      print(f"User {username} inserted successfully.")

    frontend_url = "http://localhost:3000/home"
    response = RedirectResponse(url=frontend_url)
    response.set_cookie(
      key="spotify_jwt",
      value=jwt_token,
      httponly=True,
      secure=False,
      samesite="Lax",
      max_age=60 * 60,
    )
    print("Cookie set successfully.")
    return response
  except Exception as e:
    print(f"Error in callback: {e}")
    raise HTTPException(status_code=500, detail=str(e))

@router.get("/user")
async def get_user(payload: dict = Depends(jwt_middleware_config)):
  return payload

  