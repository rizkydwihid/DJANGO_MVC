from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone

from django.db import models

# Create your models here.

class Hewan(models.Model):
    name = models.CharField(max_length=50)
    species = models.TextField(max_length=100)
    berat = models.CharField(max_length=50)
    umur = models.IntegerField()

    def __str__(self):
        return self.name

class Kandang(models.Model):
    name = models.CharField(max_length=50)
    isi_kandang = models.CharField(max_length=255)
    luas_kandang = models.CharField(max_length=50)

class Penjaga(models.Model):
    name = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=25)
    jadwal_jaga = models.TextField(max_length=50)

class Pengunjung(models.Model):
    name = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=25)
    hari_berkunjung = models.DateTimeField(default=timezone.now)