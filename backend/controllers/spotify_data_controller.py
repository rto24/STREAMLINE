import requests
from backend.config import SPOTIFY_TOP_TRACKS_URL, SPOTIFY_TOP_ARTISTS_URL, SPOTIFY_AUDIO_FEATURES_URL

def get_user_top_tracks(access_token: str, limit=50) -> list:
  response = requests.get(
    SPOTIFY_TOP_TRACKS_URL,
    params={"limit": limit},
    headers={
      "Authorization": f"Bearer {access_token}"
    }
  )
  data = response.json().get("items", [])
  print("User top tracks data:", data)
  return data

def get_user_top_artists(access_token: str, limit=50) -> list:
  response = requests.get(
    SPOTIFY_TOP_ARTISTS_URL,
    params={"limit": limit},
    headers={
      "Authorization": f"Bearer {access_token}"
    }
  )
  data = response.json().get("items", [])
  print("User top artists:", data)
  return data

def get_user_audio_metadata(access_token: str, track_ids: list) -> list:
  response = requests.get(
    SPOTIFY_AUDIO_FEATURES_URL,
    params={"ids": ",".join(track_ids)},
    headers={
      "Authorization": f"Bearer {access_token}"
    }
  )
  data = response.json().get("audio_features", [])
  print("User audio metadata:", data)
  return data
 
