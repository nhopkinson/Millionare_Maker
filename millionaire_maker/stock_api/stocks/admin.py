from django.contrib import admin
from .models import Stock, HistoricalPrice, UserProfile

# Register your models here.
admin.site.register(Stock)
admin.site.register(HistoricalPrice)
admin.site.register(UserProfile)
