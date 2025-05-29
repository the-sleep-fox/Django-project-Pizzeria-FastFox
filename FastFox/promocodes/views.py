from django.shortcuts import render
from .models import PromoCode
# Create your views here.

def promocodes(request):
    promos = PromoCode.objects.all()
    return render(request, 'promocodes/promocodes.html', {'promos': promos})
