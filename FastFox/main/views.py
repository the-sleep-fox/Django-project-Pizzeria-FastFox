import requests
from django.shortcuts import render

import news
from main import settings
from Pizza.models import Pizza
from news.models import Articles

WEATHER_API_KEY ='223aceb73cbe01a2e2ab28cd5819cb4a'

def index(request):
    last_news = Articles.objects.order_by('-date').first()
    return render(request, 'main/main_page.html', {
        'last_news': last_news
    })

def get_weather(city="Minsk"):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q=Minsk&limit=2&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }
    except requests.RequestException as e:
        print("Ошибка:", e)
        return None

print(get_weather("Minsk"))


def about(request):
    return render(request, 'main/about.html')