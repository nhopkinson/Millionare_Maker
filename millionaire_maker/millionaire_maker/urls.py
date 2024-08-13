"""
URL configuration for millionaire_maker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from . import views
from .views import line_chart, line_chart_json, fh_financials_view, fh_company_news

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about),
    path("about/", views.about),
    path("admin/", admin.site.urls),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    path('financials/', fh_financials_view, name='financials'),
    path('company_news/', fh_company_news, name='company_news'),
    #path('live_data/', real_time_data, name='live_data'),
]
