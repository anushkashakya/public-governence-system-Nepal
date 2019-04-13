from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	# mobile_no = forms.CharField(max_length=15,help_text='Valid mobile number')
	first_name = forms.CharField(max_length=128)
	last_name = forms.CharField(max_length=128)

	class Meta:
		model = User
		fields = ['username','first_name','last_name' ,'email','password1', 'password2']

	# def clean_mobile_no(self):
	# 	mobile = self.cleaned_data.get('mobile_no')
	# 	is_number_used = Profile.objects.filter(contact_no=mobile).exists()
	# 	print(is_number_used)
	# 	if is_number_used:
	# 		raise ValidationError(
	# 					('Phone no : %(value)s already used!'),
	# 					params={'value': mobile},
	# 					)
	# 	else:
	# 		return mobile

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("This Email-id is already registered.")



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	# mobile_no = forms.CharField(max_length=15)
	first_name = forms.CharField(max_length=128)
	last_name = forms.CharField(max_length=128)
	

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']