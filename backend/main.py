import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from backend.routes.auth_routes import router as auth_router
from backend.db.supabase_client import supabase

sys.path.append(str(Path(__file__).resolve().parent))
app = FastAPI()

# Register routers
app.include_router(auth_router, prefix="/auth")

# Root endpoint
@app.get("/")
async def root():
  return {"message": "Welcome to the Spotify Authentication App"}
  
@app.get("/ping-supabase")
async def ping_supabase():
  try:
    # Make a basic request to Supabase (fetches settings as a quick check)
    response = supabase.table("people").select("*").limit(1).execute()
    print(response)
    return {"message": f"{response}"}
    # Check if there is an error in the response
    if response.error:
      raise HTTPException(status_code=500, detail=f"Supabase error: {response.error.message}")
      # raise BaseException()
    
      return {"message": "Supabase connection successful", "data": response}
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to connect to Supabase: {str(e)}")
    # raise BaseException()