import pprint

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Pizza.models import Pizza
from .forms import CartAddForm
from .models import CartItem


@login_required
def add_to_cart(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)

    if request.method == 'POST':
        form = CartAddForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                pizza=pizza,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return redirect('cart:cart_detail')  # Перенаправляем в корзину
    else:
        form = CartAddForm()

    return render(request, 'cart/add_to_cart.html', {'pizza': pizza, 'form': form})


@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart:cart_detail')


@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart:cart_detail')

@login_required
def update_quantity(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id)
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity > 0:
                item.quantity = quantity
                item.save()
        except ValueError:
            pass
    return redirect('cart:cart_detail')
