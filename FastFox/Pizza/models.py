from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField()
    size = models.CharField(
        max_length=10,
        choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    )

    def __str__(self):
        return f"{self.name} ({self.get_size_display()})"


class ExtraIngredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
