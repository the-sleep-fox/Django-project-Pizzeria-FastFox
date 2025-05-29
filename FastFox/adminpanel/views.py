import statistics

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Cart.models import CartItem
from Order.models import Order, OrderItem
from reviews.models import Reviews
from django.db.models import Count, Avg, Sum, F
from .forms import PizzaForm

@staff_member_required
def dashboard(request):
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_reviews = Reviews.objects.count()
    avg_rating = Reviews.objects.aggregate(Avg('rating'))['rating__avg'] or 0

    # Считаем сумму по каждому заказу
    orders = Order.objects.prefetch_related('items')
    order_totals = []
    for order in orders:
        total = sum(item.pizza.price * item.quantity for item in order.items.all())
        order_totals.append(total)

    # Общая сумма продаж
    total_sales_sum = round(sum(order_totals), 2)

    # Статистика по продажам
    avg_sales = round(statistics.mean(order_totals), 2) if order_totals else 0
    med_sales = round(statistics.median(order_totals), 2) if order_totals else 0
    try:
        mode_sales = round(statistics.mode(order_totals), 2)
    except statistics.StatisticsError:
        mode_sales = '—'

    # Статистика по пользователям
    user_sales = []
    for user in User.objects.order_by('username'):
        user_orders = orders.filter(user=user)
        user_total = 0
        for order in user_orders:
            user_total += sum(item.pizza.price * item.quantity for item in order.items.all())
        user_sales.append({'username': user.username, 'total_sales': round(user_total, 2)})

    # Популярные пиццы по размеру
    popular_types = (
        OrderItem.objects.values('pizza__size')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    # Прибыль по name
    profit_by_type = (
        OrderItem.objects
        .values('pizza__name')
        .annotate(profit=Sum(F('pizza__price') * F('quantity')))
    )

    context = {
        'total_users': total_users - 1,
        'total_orders': total_orders,
        'total_reviews': total_reviews,
        'avg_rating': round(avg_rating, 2),
        'total_sales_sum': total_sales_sum,
        'avg_sales': avg_sales,
        'med_sales': med_sales,
        'mode_sales': mode_sales,
        'user_sales': user_sales,
        'popular_types': popular_types,
        'profit_by_type': profit_by_type,
        'avg_age': 'Нет данных',
        'med_age': 'Нет данных',
    }

    return render(request, 'adminpanel/dashboard.html', context)




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from Order.models import Order

@staff_member_required
def manage_orders(request):
    orders = Order.objects.all().select_related('user').prefetch_related('items').order_by("-created_at")

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        action = request.POST.get('action')

        order = get_object_or_404(Order, id=order_id)

        if action == 'delete':
            order.delete()
        elif action == 'mark_completed':
            order.status = 'completed'
            order.save()

        return redirect('manage_orders')

    return render(request, 'adminpanel/manage_orders.html', {'orders': orders})


@staff_member_required
def add_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PizzaForm()

    return render(request, 'adminpanel/add_pizza.html', {'form': form})