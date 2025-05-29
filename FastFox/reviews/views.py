from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Reviews
from .forms import ReviewsForm
from django.contrib.auth.decorators import login_required



@login_required()
def create_review(request):
    error = ''
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # обязательно привязываем пользователя
            review.save()
            return redirect('see_reviews')
        else:
            error = "Invalid form"
            # возвращаем форму с ошибками обратно в шаблон
            data = {
                'form': form,
                'error': error,
            }
            return render(request, 'reviews/create_review.html', data)
    else:
        form = ReviewsForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'reviews/create_review.html', data)
def see_reviews(request):
    reviews = Reviews.objects.order_by('-created_at')[:20]
    return render(request, 'reviews/see_reviews.html', {'reviews': reviews})