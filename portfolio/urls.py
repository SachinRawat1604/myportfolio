from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('certifications/', views.certifications, name='certifications'),
    path('contact/', views.contact, name='contact'),
]
