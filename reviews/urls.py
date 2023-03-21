from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thanks", views.ThankYouView.as_view()),
    # path("", views.review),
    # path("thanks", views.thankyou)

]
