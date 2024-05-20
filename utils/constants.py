import os
from dotenv import load_dotenv
import pydantic
from pydantic import BaseModel
load_dotenv()
# Retrieving data from Coca cola
params = {
  'access_key': os.getenv("MARKETSTACK_API_KEY"),
  'symbols': "KO",
  'date_from': "2020-05-08",
  'date_to': "2024-05-17"
}
column_list = [
  'open',
  'high',
  'low',
  'close',
  'volume',
  'adj_high',
  'adj_low',
  'adj_close',
  'adj_open',
  'adj_volume',
  'split_factor',
  'dividend',
  'symbol',
  'exchange',
  'date'
  ]
class MarketStackAPI(BaseModel):
  symbol: str
  high: float
  date: str



