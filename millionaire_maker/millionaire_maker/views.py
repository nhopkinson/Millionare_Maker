from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic import FormView
from .fh_client import fh_client
from .forms import StockSymbolForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from users.models import Member

from .forms import MemberForm

def index(request):
    return render(request, 'index.html')


def about(request):
    all_members = Member.objects.all
    return render(request, 'about.html', {'all': all_members})

def join(request):
    if request.method == "POST":
    # if its a post request (comes from the join.html) its doing something with the form,
    # if its something else we just return get request for the join html
        form = MemberForm(request.POST )
        if form.is_valid():
            form.save()
    else:
        form = MemberForm()
    return render(request,'join.html', )


# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]
#
#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Central", "Eastside", "Westside"]
#
#     def get_data(self):
#         """Return 3 datasets to plot."""
#
#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]
#
#
# line_chart = TemplateView.as_view(template_name='line_chart.html')
# line_chart_json = LineChartJSONView.as_view()


# FinnHub View Class
class FinancialsView(View):
    def get(self, request):
        form = StockSymbolForm()  # Instantiate the form
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = StockSymbolForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker_symbol']  # Get the ticker from the form
            financials_data = fh_client.get_basic_financials(ticker)
            quote_data = fh_client.get_quote(ticker)

            if quote_data:
                current_price = quote_data['c']
                previous_close = quote_data['pc']
                change = current_price - previous_close
                percent_change = (change / previous_close) * 100
            else:
                current_price = previous_close = change = percent_change = None

            context = {
                'form': form,
                'ticker_symbol': ticker,
                'financials': financials_data,
                'quote': {
                    'c': current_price,
                    'pc': previous_close,
                    'change': change,
                    'percent_change': percent_change,
                    'h': quote_data.get('h'),
                    'l': quote_data.get('l'),
                    'o': quote_data.get('o')
                }
            }
        else:
            context = {'form': form}

        return render(request, 'index.html', context=context)


class CompanyNewsView(View):
    def get(self, request):
        ticker = request.GET.get('ticker')
        company_news = None
        if ticker:
            from_date = "2024-06-01"
            to_date = "2024-06-02"
            company_news = fh_client.get_company_news(ticker, from_date=from_date, to_date=to_date)

        context = {
            'company_news': company_news
        }

        return render(request, 'company_news.html', context=context)


fh_financials_view = FinancialsView.as_view()
fh_company_news = CompanyNewsView.as_view()


