from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('about/', views.about, name='homepage-about'),
    path('add_complaint/', views.add_complaint, name='homepage-add_complaint'),
    path('status/', views.complaint_status, name='homepage-status'),
]