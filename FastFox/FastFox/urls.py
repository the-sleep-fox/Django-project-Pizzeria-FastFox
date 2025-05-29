"""
URL configuration for FastFox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from webbrowser import register

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('reviews/', include('reviews.urls')),
    path('contacts/', include('contacts.urls')),
    path('promocodes/', include('promocodes.urls')),
    path('offers/', include('offers.urls')),
    path('questions/', include('questions.urls')),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders/', include('Order.urls')),
    path('cart/', include('Cart.urls')),
    path('pizza/', include('Pizza.urls')),
    path('adminpanel/', include('adminpanel.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
