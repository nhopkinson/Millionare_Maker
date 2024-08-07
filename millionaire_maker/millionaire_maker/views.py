from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from polygon import RESTClient
from .client import stock_client
from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

# STOCK APP VIEW
class StockView(TemplateView):
    def market_view(self, request):
        ticker = "AAPL"
        from_date = "2023-01-01"
        to_date = "2023-01-02"
        aggregates = stock_client.get_aggregates(ticker, from_date, to_date)
        last_trade = stock_client.get_last_trade(ticker)
        trades = stock_client.list_trades(ticker, "2022-01-04")
        last_quote = stock_client.get_last_quote(ticker)
        quotes = stock_client.list_quotes(ticker, "2022-01-04")

        context = {
            'aggregates': [10, 20, 30],
            'last_trade': 45,
            'trades': [10, 20, 30],
            'last_quote': 45,
            'quotes': [10, 20, 30]
        }
        return render(request, 'test.html', context=context)


stock_view = StockView.as_view(template_name='test.html')


