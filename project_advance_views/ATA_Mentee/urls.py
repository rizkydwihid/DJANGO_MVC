from django.urls import path
from . import views

urlpatterns = [
    path('mentee', views.pagementee, name='mentee'),
]