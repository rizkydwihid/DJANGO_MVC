from django.contrib import admin
from .models import Direksi, Mentee, MataPelajaran, Mentor, Challenge, Live_Code

# Register your models here.
my_model = [Direksi, Mentee, MataPelajaran, Mentor, Challenge, Live_Code]
admin.site.register(my_model)