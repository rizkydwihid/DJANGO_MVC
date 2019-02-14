from django.shortcuts import render, redirect
from .form import PostForm
from .models import Blog
from django.utils import timezone

# Create your views here.
def pageblog(request):
    blog = Blog.objects.all()
    return render(request, 'blogpage/blog.html', {'blog':blog})

def form(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blogpage/form_page.html', {'form': form})