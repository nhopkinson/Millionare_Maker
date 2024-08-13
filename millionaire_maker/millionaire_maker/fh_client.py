import finnhub
import os
from dotenv import load_dotenv

load_dotenv()


class FinnHubCLient:
    def __init__(self, api_key):
        self.finnhub_client = finnhub.Client(api_key=api_key)

    def get_basic_financials(self, ticker):
        financials_data = self.finnhub_client.company_basic_financials(ticker, "all")
        return financials_data

    def get_company_news(self, ticker, from_date, to_date):
        company_news = self.finnhub_client.company_news(ticker, _from=from_date, to=to_date)
        return company_news

    def get_quote(self, ticker):
        quote_data = self.finnhub_client.quote(ticker)
        return quote_data


api_key = os.getenv("FINNHUB_API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set")

fh_client = FinnHubCLient(api_key)