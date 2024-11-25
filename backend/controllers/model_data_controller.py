from fastapi import HTTPException, Request
from backend.scripts.infer import generate_recommendations

async def get_recommendations(request: Request):
  try:
    body = await request.json()
    input_text = body.get("input_text")
    if not input_text:
      raise HTTPException(status_code=400, detail="input_text is required")
    
    recommendations = generate_recommendations(input_text)
    if not recommendations:
      raise HTTPException(status_code=500, detail="Failed to get reccs")
    return {"recommendations": recommendations}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))