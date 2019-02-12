from django.shortcuts import render

# Create your views here.
def pagementor(request):
    return render(request, 'ment/mentor.html', {})