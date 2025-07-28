from django.shortcuts import render, get_object_or_404
from .models import Service


def home(request):
    return render (request,"index.html",{'active': 'home'})

def about_us(request):
    return render(request, 'about_us.html', {'active': 'about'})

def our_services(request):
    return render(request, 'our_services.html', {'active': 'services'})

def blog(request):
    return render(request, 'blog.html', {'active': 'blog'})

def contact_us(request):
    return render(request, 'contact_us.html', {'active': 'contact'})

def service_details(request):
    return render(request, 'service_details.html', {'active': 'service-details'})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html', {'service': service})



def our_services(request):
    services = Service.objects.all()
    return render(request, 'our_services.html', {
        'services': services,
        'active': 'services'  # This enables the yellow underline
    })


def procurement_training(request):
    return render(request, 'services/procurement-training.html')

def procurement_audit(request):
    return render(request, 'services/procurement-audit.html')

def fraud_risk(request):
    return render(request, 'services/fraud-risk.html')

def monitoring(request):
    return render(request, 'services/monitoring.html')

def implementation_audit(request):
    return render(request, 'services/implementation-audit.html')

def success(request):
    return render(request, 'success.html')






from django.shortcuts import render, redirect
from django.contrib import messages  # very important!

from .models import ContactMessage
from django.core.mail import send_mail

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print("Form received:", name, email, subject, message)

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            full_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
            send_mail(
                subject=f"New Contact Message from {name}",
                message=full_message,
                from_email=email,  # who sent the email (user)
                recipient_list=['charitymuthoka2019@gmail.com'],  
                fail_silently=False,
            )


        
        messages.success(request, "Thanks for contacting us! We will get back to you soon.")
        return redirect('contact_us')  

    return render(request, 'contact_us.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscriber
 

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        print("Newsletter subscription:", email)

        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)


        messages.success(request, "Thank you for subscribing!")
        return redirect('contact_us') 
    return redirect('contact_us')






