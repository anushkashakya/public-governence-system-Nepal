from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from homepage.models import Complaints

class ComplaintsForm(forms.ModelForm):
	
	class Meta:
		model = Complaints
		exclude = ('solved', 'comment', 'preference')

class StatusForm(forms.Form):
    idnumber = forms.IntegerField()

    def clean_idnumber(self):
    	idnumber = self.cleaned_data['idnumber']
    	try:
    		Complaints.objects.get(pk=idnumber)
    		return idnumber
    	except Complaints.DoesNotExist:
    		raise forms.ValidationError("This Complaint ID doesn't exist. Enter Valid one !!")
		