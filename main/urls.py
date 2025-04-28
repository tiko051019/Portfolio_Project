from django.urls import path
from .views import *


handler404 = 'main.views.Page404'
urlpatterns = [
    path('portfolio/',PortfolioListView.as_view(),name = 'portfolio'),]