from django.urls import path
from .views import index, about, liveStream, services

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('livestream/', liveStream, name="live"),
    path('services/', services, name="services"),
]