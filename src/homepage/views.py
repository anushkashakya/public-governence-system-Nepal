from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from homepage.forms import ComplaintsForm
from homepage.models import Complaints
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request,'homepage/home.html',{ 'title' : 'homepage' })

def about(request):
	return render(request,'homepage/about.html', { 'title' : 'About' })

# def add_complaint(request):
# 	if request.method == 'POST':
# 		form = ComplaintsForm(request.POST) 
# 		if form.is_valid():
# 			forid =form.save()
# 			valueid = forid.id
# 			messages.success(request, f'Complaint created for {username}!')
			
# 			return render(request, 'homepage/home.html', {'valueid':valueid,'ac':"active"})
# 		else:
# 			print (form.errors)
# 	else:
# 			# If the request was not a POST, display the form to enter details.
# 		form = ComplaintsForm()

# 	return render(request, 'homepage/add_complaint.html', {'form': form, 'ac':"active"})


	 

def add_complaint(request):
	if request == 'POST':
		return render(request, 'homepage/home.html', {'valueid':valueid,'ac':"active"})
	else:
		form =  ComplaintsForm()
	return render(request, 'homepage/add_complaint.html', {'form': form, 'ac':"active"})


def complaint_status(request):
	if request.method == 'POST':
			form = StatusForm(request.POST) 
			if form.is_valid():
				cd = form.cleaned_data['idnumber']
				#idnumber  = cd.get('idnumber')
				status = Complaints.objects.get(pk=cd)
				form = StatusForm()
				# After submission of complaint user will be shown homepage
				return render(request,'homepage/complaint_status.html', {'form':form, 'status':status, 'cs':"active"})
	else:
			# If the request was not a POST, display the form to enter details.
		form = StatusForm()
	return render(request, 'homepage/complaint_status.html', {'form':form, 'cs':"active"})

