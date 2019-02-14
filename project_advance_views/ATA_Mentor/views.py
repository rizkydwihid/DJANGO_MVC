from .models import Mentor
from django.shortcuts import render

# Create your views here.
def pagementor(request):
    mentor = Mentor.objects.all()
    return render(request, 'ment/mentor.html', {'mentor':mentor})