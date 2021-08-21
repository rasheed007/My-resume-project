from core.forms import ContactForm
from django.shortcuts import render, redirect  
from .models import Contact
from django.contrib import messages 
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.


def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)




#def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse("<h3> THANKS FOR CONTACTING US</h3>")

    return render(request, 'core/contact.html')
    
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')
            send_mail(
                name,
                message,
                subject,
                email,
                '',
                fail_silently=False,
            )
            
            return redirect('core/contact.html')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)