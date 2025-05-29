from django.contrib.auth.models import User
from django.db import models


from django.db import models
from django.contrib.auth.models import User
from Pizza.models import Pizza, ExtraIngredient

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.pizza.price * self.quantity

    def __str__(self):
        return f"{self.pizza.name} x {self.quantity}"