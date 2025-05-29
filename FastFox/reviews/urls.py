from . import views
from django.urls import path

urlpatterns = [
    path('', views.see_reviews, name='see_reviews'),
    path('create/', views.create_review, name='create_review')
]
