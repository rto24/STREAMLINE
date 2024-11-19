import requests
from jose import JWTError, jwt
import datetime
from backend.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, JWT_SECRET, JWT_ALGORITHM, SPOTIFY_AUTH_URL, SPOTIFY_TOKEN_URL
import base64

SCOPE = "user-top-read user-read-recently-played playlist-modify-public"
JWT_EXPIRATION_MINUTES = 60

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
  
  if "access_token" not in token_data:
    raise Exception("Failed to fetch tokens")
  
  access_token = token_data["access_token"]
  
  profile_response = requests.get(
    "https://api.spotify.com/v1/me",
    headers={"Authorization": f"Bearer {access_token}"}
  )
  profile_data = profile_response.json()
  
  payload = {
    "sub": profile_data["id"],
    "general": profile_data,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXPIRATION_MINUTES),
    "iat": datetime.datetime.utcnow(),
    "spotify_access_token": access_token,
    "spotify_refresh_token": token_data.get("refresh_token"),
  }
  
  jwt_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  return {
        "jwt_token": jwt_token,
        "profile_data": profile_data,
        "access_token": access_token,
        "refresh_token": token_data.get("refresh_token"),
    }