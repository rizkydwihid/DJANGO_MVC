from django.urls import path
from . import views

urlpatterns = [
    path('', views.pageauthor, name='author'),
]