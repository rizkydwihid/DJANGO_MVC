from django.shortcuts import render
from .models import Mentee

# Create your views here.
def pagementee(request):
    mentee = Mentee.objects.all()
    return render(request, 'mente/mentee.html', {'mentee':mentee})