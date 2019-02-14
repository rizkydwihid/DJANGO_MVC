from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models

# Create your models here.
class Mentor(models.Model):
    gambar = models.ImageField()
    name = models.CharField(max_length=50)
    pengalaman = models.CharField(max_length=100)
    pesan = models.TextField(max_length=255)

    def __str__(self):
        return self.pengalaman