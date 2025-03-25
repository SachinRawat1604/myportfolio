from django.shortcuts import render

def home(request):
    return render(request, 'base.html')  # This now includes About, Education, Skills

def projects(request):
    return render(request, 'projects.html')

def experience(request):
    return render(request, 'experience.html')

def certifications(request):
    return render(request, 'certifications.html')


def contact(request):
    if request.method == 'POST':
        # handle form submission here (save or email)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Contact form submitted by {name} ({email}): {message}")
        # You can add email sending or DB saving here
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
