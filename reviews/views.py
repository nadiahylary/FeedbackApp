from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review


# Create your views here.


def review(request):
    # if request.method == "POST":
    #     entered_username = request.POST["username"]
    #     if entered_username == "":
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })
    #     return HttpResponseRedirect("/thanks")
    # return render(request, "reviews/review.html", {
    #     "has_error": True
    # })
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            saved_review = Review(username=form.cleaned_data['user_name'], review=form.cleaned_data['review'],
                                  rating=form.cleaned_data['rating'])
            saved_review.save()
            return HttpResponseRedirect("/thanks")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thankyou(request):
    return render(request, "reviews/thankyou.html")
