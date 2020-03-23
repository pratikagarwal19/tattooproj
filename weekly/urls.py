from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.weekly, name='weekly'),
    path('artist', views.get_artist, name='artist'),
    path('appointment', views.get_appointments, name='appointments')
]