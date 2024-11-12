from supabase import create_client, Client
from backend.config import SUPABASE_URL, SUPABASE_KEY
from dotenv import load_dotenv
import os

load_dotenv()

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)