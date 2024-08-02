from django.urls import path
from .views import StockView

urlpatterns = [
    path('stocks/', StockView.as_view(), name='stock_view'),
]
