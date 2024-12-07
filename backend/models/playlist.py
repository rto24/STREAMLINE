from pydantic import BaseModel
from typing import List

class SongData(BaseModel):
  artist: str
  name: str
  img: str
  ctaLink: str
  
class PlaylistRequestBody(BaseModel):
  playlists: List[SongData]