from django.urls import path

from adminpanel import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('orders/', views.manage_orders, name='manage_orders'),
    path('add_pizza/', views.add_pizza, name='add_pizza'),
]