from django.urls import path
from .views import contact_us_view

urlpatterns = [
    path('contact_us/', contact_us_view, name='contact_us'),
]
