from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.pageblog, name='blog'),
    path('form/', views.form, name='form'),
]