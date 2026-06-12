from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.views.decorators.csrf import csrf_exempt
from .models import Review

@csrf_exempt
def review_form(request):
    if request.method == "GET":
        return review_get(request)
    elif request.method == "POST":
        return review_post(request)
    
    return review_get(request)

def review_post(request):
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save()

    return redirect(f'/reviews/{review.id}')

def review_get(request):
    return render(request, "pages/review/review_form.html", {"form" : ReviewForm()})


def review_info(request, review_id):

    review = Review.objects.get(id = review_id)

    return render(request, "pages/review/review_info.html", {"review" : review})

def reviews(request):

    all_reviews = list(Review.objects.all())

    return render(request, "pages/reviews/reviews.html", {"reviews" : all_reviews})