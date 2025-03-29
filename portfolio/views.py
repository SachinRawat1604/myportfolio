from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from decouple import config

def home(request):
    return render(request, 'base.html') 
def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def experience(request):
    return render(request, 'experience.html')

def certifications(request):
    return render(request, 'certifications.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_mail(
            subject=f'Contact Form Submission from {name}',
            message=message,
            from_email=email,
            recipient_list=[config('EMAIL_HOST_USER')],
        )
        
        success = True

    return render(request, 'contact.html', {'success': success})

