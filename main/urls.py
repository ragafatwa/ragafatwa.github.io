from django.urls import path
from . import views
from .views import contactView, successView

urlpatterns = [
    path("", views.index, name="index"), 
    path("project/", views.project, name="project"), 
    path("artwork/", views.artwork, name="artwork"), 
    path("contact/", views.contact, name="contact"),
    path("success/", views.success, name="success"),
    #artwork 
    path("artwork-1/", views.artwork_1, name="artwork_1"), 
    path("artwork-2/", views.artwork_2, name="artwork_2"), 
    path("artwork-3/", views.artwork_3, name="artwork_3"), 
]
 