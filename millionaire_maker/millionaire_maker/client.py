from polygon import RESTClient
import os
from dotenv import load_dotenv

load_dotenv()


class StockClient:
    def __init__(self, api_key):
        self.client = RESTClient(api_key)

    def get_aggregates(self, ticker, from_date, to_date, multiplier=1,
                       timespan="minute", limit=50000):
        agg = []
        for a in self.client.list_aggs(ticker=ticker, multiplier=multiplier,
                       timespan=timespan, from_=from_date, to=to_date, limit=limit):
            agg.append(a)

        return agg

    def get_last_trade(self, ticker):
        return self.client.get_last_trade(ticker=ticker)

    def list_trades(self, ticker, timestamp):
        return list(self.client.list_trades(ticker=ticker, timestamp=timestamp))

    def get_last_quote(self, ticker):
        return self.client.get_last_quote(ticker=ticker)

    def list_quotes(self, ticker, timestamp):
        return list(self.client.list_quotes(ticker=ticker, timestamp=timestamp))


api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set")

stock_client = StockClient(api_key)