import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from backend.routes.auth_routes import router as auth_router
from backend.db.supabase_client import supabase
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(str(Path(__file__).resolve().parent))
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router, prefix="/auth")

# Root endpoint
@app.get("/")
async def root():
  return {"message": "Welcome to the Spotify Authentication App"}
