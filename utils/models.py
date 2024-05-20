import pydantic
from pydantic import BaseModel

class MarketStackAPI(BaseModel):
  symbol: str
  high: float
  date: str
