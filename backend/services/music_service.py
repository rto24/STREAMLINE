import re
from backend.controllers.spotify_data_controller import search_song
from backend.scripts.infer import generate_recommendations
from backend.scripts.fetch_data import fetch_user_data

def extract_songs_from_text(generated_text: str):
  """Extract song and artist information from the generated text."""
  print(generated_text)
  pattern = r'\d+\.\s+"(.+?)"\s+by\s+([\w\s&]+)\s+-'
  matches = re.findall(pattern, generated_text)
  print("Matches:", matches)
  
  recommended_songs = []
  for song, artist in matches:
    recommended_songs.append({
      "song": song,
      "artist": artist
    })
  return recommended_songs

async def get_songs(access_token: str):
  """Asynchronous function to fetch user data, generate recommendations, and extract songs."""
  try:
    user_data = await fetch_user_data(access_token)
    generated_text = await generate_recommendations(user_data["reformatted_data"][0]["input"])
    recommended_songs = extract_songs_from_text(generated_text)
    
    searched_songs = []
    for recommendation in recommended_songs:
      song_name = recommendation["song"]
      artist_name = recommendation["artist"]
      returned_song = search_song(access_token, song_name, artist_name)
      searched_songs.append(returned_song)
      
    return searched_songs
  except Exception as e:
    print(f"Error in get_songs: {e}")
    return []