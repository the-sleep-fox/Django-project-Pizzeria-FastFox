from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewsForm

# Create your views here.
def create_review(request):
    error = ''
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_review')
        else:
            error = "Invalid form"
    form = ReviewsForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'reviews/create_review.html', data)

def see_reviews(request):
    reviews = Reviews.objects.order_by('-date')[:20]
    return render(request, 'reviews/see_reviews.html', {'reviews': reviews})