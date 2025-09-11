from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('<int:pk>', views.AnswerDetailView.as_view(), name='answer-details'),
]