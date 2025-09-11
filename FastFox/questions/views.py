from django.shortcuts import render
from django.views.generic import DetailView

from .models import Questions
# Create your views here.

def questions(request):
    quests = Questions.objects.order_by('date')[ :5]
    return render(request, 'questions/questions.html', {'quests': quests})

class AnswerDetailView(DetailView):
    model = Questions
    template_name = 'questions/detail_answer.html'
    context_object_name = "answer"

