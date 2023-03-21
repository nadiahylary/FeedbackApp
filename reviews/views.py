from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .forms import ReviewForm
from .models import Review


# Create your views here.

# This method: class-based view
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thanks")
        return render(request, "reviews/review.html", {
            "form": form
        })


# OR
# This method:
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
        # To update an existing review record:
        # existing_review = Review.objects.get(id=1)
        # form = ReviewForm(request.POST, instance=existing_review)
        # To create a new review record:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # using the ModelForm
            # saved_review = Review(username=form.cleaned_data['user_name'], review=form.cleaned_data['review'],
            #                       rating=form.cleaned_data['rating'])
            # saved_review.save()
            return HttpResponseRedirect("/thanks")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thankyou.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "It works! Fantastic!"
        return context


# def thankyou(self, request):
#     return render(request, "reviews/thankyou.html")
