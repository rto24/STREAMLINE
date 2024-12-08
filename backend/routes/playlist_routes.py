from fastapi import APIRouter, Depends, HTTPException
from backend.middleware.auth_middleware import jwt_middleware_access_token
from backend.db.supabase_client import update_user_playlist, get_user_by_username, get_user_playlist
from backend.models.playlist import PlaylistRequestBody
from backend.controllers.playlist_controller import save_playlist_controller

router = APIRouter()

@router.post("/{username}")
async def save_song_to_user_playlist(username: str, body: PlaylistRequestBody):
  try:
    return await save_playlist_controller(username, body)
  except Exception as e:
    print("Error in playlist route:", str(e))
    raise HTTPException(status_code=500, detail=str(e))

@router.get("/{username}")
def get_user_saved_songs(username: str):
  return get_user_playlist(username)