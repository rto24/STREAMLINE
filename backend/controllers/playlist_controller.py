from fastapi import HTTPException
from backend.db.supabase_client import update_user_playlist, get_user_by_username
from backend.models.playlist import PlaylistRequestBody

async def save_playlist_controller(username: str, body: PlaylistRequestBody):
  try:
    user = get_user_by_username(username)

    if not user:
      raise HTTPException(status_code=404, detail="User not found")

    updated_playlist = user.get("playlists", []) + [song.dict() for song in body.playlists]
    print("UPDATED PLAYLIST", updated_playlist)

    update_user_playlist(username, updated_playlist)

    return {
      "message": f"Playlist updated for {username}",
      "playlists": updated_playlist,
    }
  except Exception as e:
    print("Error in playlist controller:", str(e))
    raise HTTPException(status_code=500, detail=str(e))