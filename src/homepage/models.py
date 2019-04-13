from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Complaints(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


	GARBAGE = 'GA'
	POTHOLES = 'PH'
	SEWAGE = 'SW'
	OTHERS = 'OT'
	TYPEOFCOMP_CHOICES = (
		(GARBAGE, 'garbage'),
		(POTHOLES, 'potholes'),
		(SEWAGE, 'sewage'),
		)
	type_of_complaint = models.CharField(max_length=2,
									choices=TYPEOFCOMP_CHOICES,
									default=OTHERS)
	image = models.ImageField(null=True,upload_to='user_upload')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title