from django.shortcuts import render

# Create your views here.
def pagementee(request):
    return render(request, 'mente/mentee.html', {})