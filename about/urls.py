from django.urls import path
from .views import about_view #, about_marketplace_view

urlpatterns = [
    path("about-us/", about_view, name="about"),
    #path("marketplace/about/", about_marketplace_view, name="about_marketplace") 
]
