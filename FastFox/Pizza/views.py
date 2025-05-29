from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Pizza
from django.contrib.auth.decorators import login_required

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/pizza_list.html', {'pizzas': pizzas})

@staff_member_required
def add_pizza():
    return None