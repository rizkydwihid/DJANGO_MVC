from django.shortcuts import render

# Create your views here.
def pageblog(request):
    return render(request, 'blogpage/blog.html', {})