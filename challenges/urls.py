from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('<int:month>', views.month_id),
    path('<str:month>', views.index),
]