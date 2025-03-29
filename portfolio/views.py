from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

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

def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f"New Contact from {name}"
        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
        success = True

    return render(request, 'contact.html', {'success': success})

