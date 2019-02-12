from django.shortcuts import render
from . import urls

# Create your views here.
def pageauthor(request):
    return render(request, 'aut/author.html', {})