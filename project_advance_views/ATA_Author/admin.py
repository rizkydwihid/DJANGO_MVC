from django.contrib import admin
from .models import Author

model_new = [Author]
admin.site.register(model_new)
# Register your models here.
