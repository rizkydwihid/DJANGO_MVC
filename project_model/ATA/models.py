from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone

from django.db import models

# Create your models here.

class Direksi(models.Model):
    nama_lengkap = models.TextField(max_length=50)
    no_telepon = models.IntegerField()
    jabatan = models.TextField(max_length=20)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.TextField(max_length=50)
    no_telepon = models.IntegerField()
    no_absen = models.IntegerField()
    nilai_rata_rata = models.IntegerField()

class MataPelajaran(models.Model):
    nama_pelajaran = models.TextField(max_length=100)
    jadwal_dimulai = models.CharField(max_length=100)
    jadwal_berakhir = models.CharField(max_length=100)

class Mentor(models.Model):
    nama_lengkap = models.TextField(max_length=50)
    no_telepon = models.IntegerField()
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete= models.CASCADE)


class Challenge(models.Model):
    nama_challenge = models.TextField(max_length=100)
    banyak_soal = models.CharField(max_length=100)
    bobot_nilai = models.CharField(max_length=100)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)


class Live_Code(models.Model):
    nama_live_code = models.TextField(max_length=50)
    banyak_soal = models.CharField(max_length=50)
    bobot_nilai = models.CharField(max_length=50)
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete= models.CASCADE)