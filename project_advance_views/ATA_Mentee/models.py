from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models

# Create your models here.
class Mentee(models.Model):
    gambar = models.ImageField()
    name = models.CharField(max_length=50)
    keterangan = models.TextField(max_length=100)

    def __str__(self):
        return self.name