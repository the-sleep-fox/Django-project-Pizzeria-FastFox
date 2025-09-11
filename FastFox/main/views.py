from django.shortcuts import render

import news
from Pizza.models import Pizza
from news.models import Articles


def index(request):
    last_news = Articles.objects.order_by('-date').first()
    return render(request, 'main/main_page.html', {
        'last_news': last_news
    })




def about(request):
    return render(request, 'main/about.html')