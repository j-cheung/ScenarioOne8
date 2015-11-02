from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class List(models.Model):
	list_title = models.CharField(max_length = 30)
	user = models.ForeignKey(User)

class Task(models.Model):
	task_title = models.CharField(max_length = 30)
	completed = models.BooleanField()
	description = models.CharField(max_length = 200)
	theList = models.ForeignKey(List)


