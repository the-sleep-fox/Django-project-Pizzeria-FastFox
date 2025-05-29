from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('success/', views.order_success, name='order_success'),
    path('history/', views.order_history, name='order_history'),
    path('my_orders/', views.my_orders, name='my_orders'),
]
