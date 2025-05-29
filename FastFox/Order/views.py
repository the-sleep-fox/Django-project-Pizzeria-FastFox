from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Cart.models import CartItem
from Cart.views import cart_detail

from .models import Order, OrderItem
from .forms import OrderCreateForm

@login_required
def create_order(request):
    cart = CartItem.objects.filter(user=request.user)
    if not cart:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    pizza=item.pizza,
                    quantity=item.quantity
                )
            cart.delete() # Очистить корзину
            return redirect('order:order_success')
    else:
        form = OrderCreateForm()

    return render(request, 'order/create_order.html', {'form': form, 'cart': cart})

@login_required
def order_success(request):
    return render(request, 'order/success.html')

@login_required
def order_history(request):
    orders = request.user.orders.prefetch_related('items__pizza')
    return render(request, 'order/history.html', {'orders': orders})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order/my_orders.html', {'orders': orders})