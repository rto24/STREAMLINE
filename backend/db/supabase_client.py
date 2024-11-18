from supabase import create_client, Client
from backend.config import SUPABASE_URL, SUPABASE_KEY
from dotenv import load_dotenv
import os

load_dotenv()

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_by_username(username: str):
  response = supabase.table("person").select("id").eq("username", username).execute()
  print("get_user_by_username response:", response)
  if not response:
    raise Exception(f"Error fetching user: {response['error']}")
  return response.data

def insert_user(username: str, playlists: list):
  print(f"Inserting user: {username}, playlists: {playlists}")
  response = supabase.table("person").insert({
    "username": username,
    "playlists": playlists
  }).execute()
  if not response:
    raise Exception(f"Error inserting user: {response['error']}")
  return response.data