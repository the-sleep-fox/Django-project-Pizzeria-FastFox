from django.shortcuts import render
from .models import Questions
# Create your views here.

def questions(request):
    quests = Questions.objects.order_by('-date')[ :20]
    return render(request, 'questions/questions.html', {'quests': quests})