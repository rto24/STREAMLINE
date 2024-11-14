import requests
from backend.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import base64

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SCOPE = "user-top-read user-read-recently-played playlist-modify-public"

async def generate_spotify_login_url():
  return (
    f"{SPOTIFY_AUTH_URL}?client_id={SPOTIFY_CLIENT_ID}"
    f"&response_type=code&redirect_uri={SPOTIFY_REDIRECT_URI}"
    f"&scope={SCOPE}"
  )

async def handle_spotify_callback(code: str):
  auth_header = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
  token_response = requests.post(
    SPOTIFY_TOKEN_URL,
    data={
      "grant_type": "authorization_code",
      "code": code,
      "redirect_uri": SPOTIFY_REDIRECT_URI
    },
    headers={
      "Authorization": f"Basic {auth_header}",
      "Content-Type": "application/x-www-form-urlencoded"
    },
  )
  token_data = token_response.json()
  return {
    "spotify_user_id": token_data["id"],
    "access_token": token_data["access_token"],
    "refresh_token": token_data["refresh_token"],
    "token_expiry": token_data["expires_in"]
  }