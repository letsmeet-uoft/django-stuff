from django.contrib.auth.models import User
from django.db import models
from schedule.models import Calendar

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)


	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return "User: " + self.first_name + " " + self.last_name

