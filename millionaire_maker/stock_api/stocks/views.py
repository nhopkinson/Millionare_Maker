from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polygon import RESTClient
from millionaire_maker.stock_api.stock_api.client import stock_client
from django.shortcuts import render


class StockView:
    def market_view(request):
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

# class StockDataView(APIView):
#     def get(self, request, symbol):
#         api_url = f"https://api.example.com/stocks/{symbol}"
#         response = requests.get(api_url)
#
#         if response.status_code == 200:
#             data = response.json()
#             serializer = StockDataSerializer(data=data)
#             if serializer.is_valid():
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"error": "Stock not found"}, status=status.HTTP_404_NOT_FOUND)
