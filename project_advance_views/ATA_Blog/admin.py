from django.contrib import admin
from .models import Blog

model_new = [Blog]
admin.site.register(model_new)
# Register your models here.
