from django.contrib import admin
from homepage.models import Complaints
from django.contrib.auth.models import User
# Register your models here.

class ComplaintsAdmin(admin.ModelAdmin):
	list_display = ('type_of_complaint', 'title', 'solved', 'preference',)

# class UserProfileAdmin(admin.ModelAdmin):
# 	list_display = ('User.username', 'User.email')

admin.site.register(Complaints,ComplaintsAdmin)
#admin.site.register(UserProfile)