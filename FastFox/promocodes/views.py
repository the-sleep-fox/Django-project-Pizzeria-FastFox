from django.shortcuts import render
from .models import Promocodes
# Create your views here.

def promocodes(request):
    promos = Promocodes.objects.all()
    return render(request, 'promocodes/promocodes.html', {'promos': promos})
