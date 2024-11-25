import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from backend.routes.auth_routes import router as auth_router
from backend.routes.spotify_data_routes import router as spotify_router
from backend.routes.model_output_routes import router as model_router
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
app.include_router(spotify_router, prefix="/spotify")
app.include_router(model_router, prefix="/model")

# Root endpoint
@app.get("/")
async def root():
  return {"message": "Welcome to the Spotify Authentication App"}
