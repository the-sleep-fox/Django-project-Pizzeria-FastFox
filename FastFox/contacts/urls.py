from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_contacts, name='get_contacts'),
]