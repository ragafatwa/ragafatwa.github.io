from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.

def index(response):
    return render(response, "main/index.html", {})
def project(response):
    return render(response, "main/project.html", {})
def artwork(response):
    return render(response, "main/artwork.html", {})
def contact(response):
    return render(response, "main/contact.html", {})
def success(response):
    return render(response, "main/contact-success.html", {})


#artwork
def artwork_1(response):
    return render(response, "main/artwork-1-detail.html", {})
def artwork_2(response):
    return render(response, "main/artwork-2-detail.html", {})
def artwork_3(response):
    return render(response, "main/artwork-3-detail.html", {})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ragafatwa@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})
 
def successView(request):
    return HttpResponse('Success! Thank you for your message.')