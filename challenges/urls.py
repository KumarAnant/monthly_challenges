from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('<int:monthid>', views.month_id),    
    path('<str:month>', views.index, name = 'month-challenge'),
]