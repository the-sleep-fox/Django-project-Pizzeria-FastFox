from django.urls import path
from . import views

app_name = 'pizza'

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('add/', views.add_pizza, name='add_pizza'),
]
