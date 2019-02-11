from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone


from django.db import models

# Create your models here.

class Mentee(models.Model):
	name = models.CharField(max_length=255)
	full_name = models.TextField(max_length=255)
	nickname = models.TextField(max_length=255)
	gender = models.CharField(max_length=1)
	telephone = models.TextField(max_length=25)
	mobile = models.TextField(max_length=25)
	address = models.TextField(max_length=255)

	def __str__(self):
		return self.name
	
class BlogPost(models.Model):
	created = models.DateTimeField(default=timezone.now)
	update = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=255)
	content = models.CharField(max_length=255)
	created_by = models.CharField(max_length=255)
	posted_by = models.ForeignKey(Mentee, on_delete=models.CASCADE)
