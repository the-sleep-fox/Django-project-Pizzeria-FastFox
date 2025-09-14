
import random
import requests
from django.shortcuts import render

from main.models import Partners
from news.models import Articles

WEATHER_API_KEY ='223aceb73cbe01a2e2ab28cd5819cb4a'

def index(request):
    last_news = Articles.objects.order_by('-date').first()
    weather = get_weather()
    partners = get_patners()
    banner_name = get_random_banner()
    return render(request, 'main/main_page.html', {
        'last_news': last_news,
        'weather': weather,
        'partners': partners,
        'banner_name': banner_name
    })

def get_weather(city="Minsk"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&limit=1&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # print(type(data))
        # print(data)

        return{
            "city": data['name'],
            'temp': round(data['main']['temp']),
            'description': data['weather'][0]['description'],
        }
    except requests.RequestException as e:
        print("Ошибка:", e)
        return None

def get_patners():
    return Partners.objects.all()

def about(request):
    return render(request, 'main/about.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def get_random_banner():
    banner_list = ["banner_1.jpeg", "banner_2.png", "banner_3.jpeg"]
    return random.choice(banner_list)


