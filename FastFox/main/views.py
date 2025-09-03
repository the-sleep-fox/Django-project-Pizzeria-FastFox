from django.shortcuts import render

from Pizza.models import Pizza


#getting a response
def index(request):
    return render(request, 'main/main_page.html')
    # pizzas = Pizza.objects.all()
    # return render(request, 'pizza/pizza_list.html', {'pizzas': pizzas})
def about(request):
    return render(request, 'main/about.html')