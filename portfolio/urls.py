from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),

]
