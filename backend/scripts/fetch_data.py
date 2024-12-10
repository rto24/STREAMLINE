import json
import os
from fastapi import Depends
from backend.controllers.spotify_data_controller import get_user_top_tracks, get_user_top_artists, get_user_audio_metadata
from backend.middleware.auth_middleware import jwt_middleware_access_token 

async def fetch_user_data(access_token: str, limit=5, output_file: str = "backend/data/train.json"):
  tracks = await get_user_top_tracks(access_token, limit=limit)
  artists = await get_user_top_artists(access_token, limit=limit)
  
  track_ids = []
  for track in tracks:
    track_ids.append(track["id"])
  song_metadata = await get_user_audio_metadata(access_token, track_ids)

  combined_track_data = []
  for track, metadata in zip(tracks, song_metadata):
    combined_track_data.append(
      f"{track['name']} (danceability: {metadata['danceability']}, tempo: {metadata['tempo']}, energy: {metadata['energy']})"
    )
  
  top_artists = []
  top_genres = set()
  for artist in artists:
    top_artists.append(artist["name"])
    top_genres.update(artist["genres"])
  
  reformatted_data = [
    {
      "input": f"User likes tracks: {', '.join(combined_track_data)}. User's top artists: {', '.join(top_artists)}. User's top genres: {', '.join(top_genres)}. Based on the user information that was just given, recommend {limit} songs that can be found on Spotify that will match user tastes. Do not repeat any songs that you have recommended already.",
      "output": "1. Song A by Artist B\n2. Song C by Artist D\n3. Song E by Arist F\n4. Song G by Artist H\n5. Song I by Arist J"
    }
  ]
  
  if os.path.exists(output_file):
    with open(output_file, "r") as f:
      existing_data = json.load(f)
  else:
    existing_data = []
  
  existing_data.extend(reformatted_data)
  
  with open(output_file, "w") as f:
    json.dump(existing_data, f, indent=4)
  
  print(f"Reformatted data saved to {output_file}")

  return {
    "tracks": combined_track_data,
    "artists": top_artists,
    "genres": top_genres,
    "reformatted_data": reformatted_data
  }
  