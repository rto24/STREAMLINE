from backend.config import SPOTIFY_TOP_TRACKS_URL, SPOTIFY_TOP_ARTISTS_URL, SPOTIFY_AUDIO_FEATURES_URL, SPOTIFY_SEARCH_SONG_URL
import requests
import asyncio

async def get_user_top_tracks(access_token: str, limit=5) -> list:
  def fetch_tracks():
    response = requests.get(
      SPOTIFY_TOP_TRACKS_URL,
      params={"limit": limit},
      headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json().get("items", [])

  return await asyncio.to_thread(fetch_tracks)

async def get_user_top_artists(access_token: str, limit=5) -> list:
  def fetch_artists():
    response = requests.get(
      SPOTIFY_TOP_ARTISTS_URL,
      params={"limit": limit},
      headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json().get("items", [])

  return await asyncio.to_thread(fetch_artists)

async def get_user_audio_metadata(access_token: str, track_ids: list) -> list:
  def fetch_metadata():
    response = requests.get(
      SPOTIFY_AUDIO_FEATURES_URL,
      params={"ids": ",".join(track_ids)},
      headers={"Authorization": f"Bearer {access_token}"}
    )
    return response.json().get("audio_features", [])

  return await asyncio.to_thread(fetch_metadata)
 
def search_song(access_token: str, song_name: str, artist_name: str):
  response = requests.get(
    SPOTIFY_SEARCH_SONG_URL,
    params={
      "q": f"track:{song_name} artist:{artist_name}",
      "type": "track",
      "limit": 1
    },
    headers={
      "Authorization": f"Bearer {access_token}"
    }
  )
  data = response.json()
  print("Song search result:", data)
  return data
