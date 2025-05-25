from .models import Reviews
from django.forms import ModelForm, TextInput, DateTimeInput

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['anons', 'full_text', 'date']
        widgets = {
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Review anons'
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input review here'
            }),
            "date": DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Input date here'
            })
        }


