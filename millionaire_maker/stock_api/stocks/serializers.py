from rest_framework import serializers
from .models import Stock


class StockDataSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=10)
    price = serializers.FloatField()
    # Add more fields as necessary
