from polygon import RESTClient
from millionaire_maker.stock_api.stock_api.client import stock_client
from django.shortcuts import render
from django.views.generic.base import TemplateView


class StockView(TemplateView):
    def market_view(self, request):
        ticker = "AAPL"
        from_date = "2023-01-01"
        to_date = "2023-06-13"

        aggregates = stock_client.get_aggregates(ticker, from_date, to_date)
        last_trade = stock_client.get_last_trade(ticker)
        trades = stock_client.list_trades(ticker, "2022-01-04")
        last_quote = stock_client.get_last_quote(ticker)
        quotes = stock_client.list_quotes(ticker, "2022-01-04")

        context = {
            'aggregates': aggregates,
            'last_trade': last_trade,
            'trades': trades,
            'last_quote': last_quote,
            'quotes': quotes
        }
        return render(request, 'test.html', context)


stock_view = TemplateView.as_view(template_name='test.html')
