from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="index"),
    path("thanks", views.ThankYouView.as_view(), name="thanks"),
    path("reviews", views.ReviewsListView.as_view(), name="reviews"),
    path("reviews/<int:id>", views.SingleReviewDetail.as_view(), name="detail-review")
    # path("", views.review),
    # path("thanks", views.thankyou)

]
