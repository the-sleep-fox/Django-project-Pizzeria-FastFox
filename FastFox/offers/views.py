from django.shortcuts import render

from .models import Offers


# Create your views here.

def offers(request):
    job_offers = Offers.objects.order_by('salary')
    return render(request, 'offers/offers.html', {'job_offers': job_offers})