import json
from fastapi import Depends
from backend.controllers.spotify_data_controller import get_user_top_tracks, get_user_top_artists
from backend.middleware.auth_middleware import jwt_middleware_access_token

def fetch_user_data(access_token: str, limit=5):
  tracks = get_user_top_tracks(access_token, limit=limit)
  print("tracks", tracks)
  
  artists = get_user_top_artists(access_token, limit=limit)

  for track in tracks:
    print(track["name"])
    print(track["uri"])

  return {
    "tracks": [{"name": track["name"], "uri": track["uri"]} for track in tracks],
    "artists": [{"name": artist["name"]} for artist in artists]
  }