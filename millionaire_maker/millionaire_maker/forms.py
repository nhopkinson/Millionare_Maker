from django import forms


class StockSymbolForm(forms.Form):
    ticker_symbol = forms.CharField(max_length=7, label= "Enter a ticker symbol")
