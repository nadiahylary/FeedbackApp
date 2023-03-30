from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thanks"
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thanks"

# OR
# This method: class-based view
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#
#         return render(request, "reviews/review.html", {
#             "form": form
#         })
#
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thanks")
#         return render(request, "reviews/review.html", {
#             "form": form
#         })


# OR
# This method:
# def review(request):
#     # if request.method == "POST":
#     #     entered_username = request.POST["username"]
#     #     if entered_username == "":
#     #         return render(request, "reviews/review.html", {
#     #             "has_error": True
#     #         })
#     #     return HttpResponseRedirect("/thanks")
#     # return render(request, "reviews/review.html", {
#     #     "has_error": True
#     # })
#     if request.method == 'POST':
#         # To update an existing review record:
#         # existing_review = Review.objects.get(id=1)
#         # form = ReviewForm(request.POST, instance=existing_review)
#         # To create a new review record:
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()  # using the ModelForm
#             # saved_review = Review(username=form.cleaned_data['user_name'], review=form.cleaned_data['review'],
#             #                       rating=form.cleaned_data['rating'])
#             # saved_review.save()
#             return HttpResponseRedirect("/thanks")
#
#     else:
#         form = ReviewForm()
#
#     return render(request, "reviews/review.html", {
#         "form": form
#     })


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thankyou.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "We appreciate you taking your time to leave us a review about how we're doing. We sure " \
                             "will make good use of your useful feedback "
        return context


# def thankyou(self, request):
#     return render(request, "reviews/thankyou.html")

# class ReviewsListView(TemplateView):
#     template_name = "reviews/reviews_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     return base_query.filter(rating__gt=3)


# class SingleReviewDetail(TemplateView):
#     template_name = "reviews/detailreview.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review = Review.objects.get(id=kwargs["id"])
#         context["review"] = review
#         return context


class SingleReviewDetail(DetailView):
    template_name = "reviews/detailreview.html"
    model = Review
    context_object_name = "review"

