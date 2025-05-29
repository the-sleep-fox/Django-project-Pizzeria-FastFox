from django import forms
from .models import Pizza

class AddToCartForm(forms.Form):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), label="Выберите пиццу")
    extra_ingredients = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Доп. ингредиенты через запятую'})
    )
    quantity = forms.IntegerField(min_value=1, initial=1, label="Количество")
