from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("artwork/", views.artwork, name="artwork"), 
    path("contact/", views.contact, name="contact"),
    #artwork 
    path("artwork-1/", views.artwork_1, name="artwork_1"), 
    path("artwork-2/", views.artwork_2, name="artwork_2"), 
    path("artwork-3/", views.artwork_3, name="artwork_3"), 
]
 