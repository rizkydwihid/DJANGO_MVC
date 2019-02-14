from .models import Author
from django.shortcuts import render

# Create your views here.
def pageauthor(request):
    author = Author.objects.all()
    return render(request, 'aut/author.html', {'author':author})