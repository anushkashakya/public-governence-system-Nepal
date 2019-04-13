from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

def validate_mobile_no_is_numeric(mobile_no):
    if not mobile_no.isnumeric():
        raise ValidationError(
            _('"%(num)s" is not valid mobile number'),
            params={'num':mobile_no }
            )

class Profile(models.Model):
	MALE = 'm'
	FEMALE = 'f'

	GENDER_CHOICE = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=128,null=True)
	last_name = models.CharField(max_length=128,null=True)
	dob = models.DateField(null=True, blank=True)
	age = models.IntegerField(default=0,null=True)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default=MALE,null=True)
	contact_no = models.CharField(max_length=15, null=True,unique=True,
								verbose_name='Mobile No',
								help_text='98XXXXXXXX',
								validators=[validate_mobile_no_is_numeric,])
	address = models.CharField(max_length=50, null=True, blank=True)
	GRA = 'GR'
	POST = 'PG'
	VOCA = 'VO'
	HIGHSEC = 'HS'
	SECOND = 'SE'
	ELEMENT = 'EL'
	NONE = 'NO'


	EDUCATION_CHOICES = (
		(GRA, 'Graduation'),
		(POST, 'Post Graduation'),
		(VOCA, 'Vocational'),
		(HIGHSEC, 'Higher Secondary'),
		(SECOND, 'Secondary'),
		(ELEMENT, 'Elementary'),
		(NONE, 'None')
		)
	education = models.CharField(max_length=8,
							choices=EDUCATION_CHOICES,
							default=NONE,null=True)
	occupation = models.CharField(max_length=20, null=True, blank=True)
	nationality = models.CharField(max_length=20, null=True, blank=True)
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	
	

	

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,*args,**kwargs):
		super(Profile,self).save(*args,**kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)