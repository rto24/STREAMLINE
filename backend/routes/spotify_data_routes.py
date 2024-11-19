from fastapi import APIRouter, HTTPException, Query, Response, Depends
from backend.middleware.auth_middleware import jwt_middleware_access_token
from backend.controllers.spotify_data_controller import get_user_top_tracks, get_user_top_artists, get_user_audio_metadata

router = APIRouter()

@router.get("/top-tracks")
async def user_top_tracks(access_token: str = Depends(jwt_middleware_access_token)):
  try:
    tracks = get_user_top_tracks(access_token)
    return {"top tracks": tracks}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.get("/top-artists")
async def user_top_artists(access_token: str = Depends(jwt_middleware_access_token)):
  try:
    artists = get_user_top_artists(access_token)
    return {"top artists": artists}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  

@router.get("/audio-metadata")
async def user_audio_metadata(access_token: str = Depends(jwt_middleware_access_token)):
  try:
    audio_metadata = get_user_audio_metadata(access_token)
    return {"audio metadata": audio_metadata}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))