from django.contrib import admin
from .models import Mentee

model_new = [Mentee]
admin.site.register(model_new)
# Register your models here.
