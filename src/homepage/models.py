from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Complaints(models.Model):
	title = models.CharField(max_length=100)
	username = models.ForeignKey(User, on_delete=models.CASCADE)


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
	complaint_des = models.TextField(null=True)
	date_posted = models.DateTimeField(default=timezone.now)

	SOLVED='SOLVED'
	UNSOLVED='NOT SOLVED'
	CON = 'UNDER CONSIDERATION'
	SOLVED_CHOICES = (
		(SOLVED, 'solved'),
		(UNSOLVED, 'unsolved'),
		(CON, 'under consideration')
		)
	solved = models.CharField(max_length=50,
							choices=SOLVED_CHOICES,
							default=UNSOLVED)
	PREFERENCE_CHOICE = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		) 
	preference = models.IntegerField(choices=PREFERENCE_CHOICE,
									default=0)
	def __unicode__(self):
		return "complain of :" + self.username

	# def __str__(self):
	# 	return self.title