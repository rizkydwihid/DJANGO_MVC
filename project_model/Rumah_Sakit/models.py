from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone

from django.db import models

# Create your models here.

class Dokter(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=25)
    bidang = models.TextField(max_length=255)
    jadwal_prakter = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Passien(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=25)
    alamat = models.TextField(max_length=255)
    keluhan = models.TextField(max_length=255)

class Resep(models.Model):
    name = models.CharField(max_length=255)
    total_harga = models.IntegerField()
    kumpulan_obat = models.TextField(max_length=255)

class Obat(models.Model):
    name = models.CharField(max_length=255)
    kandungan = models.CharField(max_length=255)
    khasiat = models.CharField(max_length=255)