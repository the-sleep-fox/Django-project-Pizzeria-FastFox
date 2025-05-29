from Pizza.models import Pizza

def get_cart(request):
    """
    Возвращает содержимое корзины как список словарей с пиццей и её количеством.
    """
    cart = request.session.get('cart', {})
    cart_items = []

    for pizza_id, quantity in cart.items():
        try:
            pizza = Pizza.objects.get(id=pizza_id)
            cart_items.append({
                'pizza': pizza,
                'quantity': quantity
            })
        except Pizza.DoesNotExist:
            continue

    return cart_items

def add_to_cart(request, pizza_id, quantity=1):
    """
    Добавляет пиццу в корзину или увеличивает её количество.
    """
    cart = request.session.get('cart', {})
    cart[str(pizza_id)] = cart.get(str(pizza_id), 0) + quantity
    request.session['cart'] = cart

def remove_from_cart(request, pizza_id):
    """
    Удаляет пиццу из корзины.
    """
    cart = request.session.get('cart', {})
    if str(pizza_id) in cart:
        del cart[str(pizza_id)]
    request.session['cart'] = cart

def clear_cart(request):
    """
    Полностью очищает корзину.
    """
    request.session['cart'] = {}
