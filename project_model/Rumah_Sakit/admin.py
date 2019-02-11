from django.contrib import admin
from .models import Dokter, Passien, Resep, Obat

# Register your models here.
my_model = [Dokter, Passien, Resep, Obat]
admin.site.register(my_model)