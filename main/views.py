from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "main/index.html", {})
def artwork(response):
    return render(response, "main/artwork.html", {})
def contact(response):
    return render(response, "main/contact.html", {})


#artwork
def artwork_1(response):
    return render(response, "main/artwork-1-detail.html", {})
def artwork_2(response):
    return render(response, "main/artwork-2-detail.html", {})
def artwork_3(response):
    return render(response, "main/artwork-3-detail.html", {})

