from django.urls import path
from . import views

urlpatterns = [
    path('', views.pageblog, name='blog'),
]