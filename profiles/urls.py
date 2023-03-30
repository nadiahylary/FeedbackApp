from django.conf.urls.static import static
from django.urls import path

from feedbackApp import settings
from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("all", views.ProfileListView.as_view())

]