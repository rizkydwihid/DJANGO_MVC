from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagehome, name='home'),
]