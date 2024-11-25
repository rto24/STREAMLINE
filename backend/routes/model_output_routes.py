from fastapi import APIRouter, Request
from backend.controllers.model_data_controller import get_recommendations

router = APIRouter()

@router.post("/recommendations")
async def recommendations_endpoint(request: Request):
  return await get_recommendations(request)