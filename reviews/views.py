from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def review(request):
    if request.method == "POST":
        entered_username = request.POST["username"]
        return HttpResponseRedirect("/thanks")
    else:
        return render(request, "reviews/review.html")


def thankyou(request):
    return render(request, "reviews/thankyou.html")
