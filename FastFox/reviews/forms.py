from .models import Reviews
from django.forms import ModelForm, TextInput, DateTimeInput
from django import forms
RATING_CHOICES = [(i, '★' * i + '☆' * (5 - i)) for i in range(1, 6)]

class ReviewsForm(ModelForm):
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        label="Review"
    )
    class Meta:
        model = Reviews
        fields = ['anons', 'full_text', 'rating']
        widgets = {
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Review anons'
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input review here'
            })
        }


