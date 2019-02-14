from django import forms

from .models import Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('gambar', 'created_at', 'judul', 'isi')