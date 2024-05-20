import pydantic


class MarketStackAPI(BaseModel):
  symbol: str
  high: float
  date: str
