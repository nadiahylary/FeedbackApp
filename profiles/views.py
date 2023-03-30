from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from profiles.forms import ProfileForm
from profiles.models import UserProfile

form = ProfileForm
# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create-profile.html", {"form": form})

    def post(self, request):
        submitted_form = form(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_file"])
            # store_files(request.FILES["uploaded"])
            profile.save()
            return HttpResponseRedirect("/profiles/")
        return render(request, "profiles/create-profile.html", {
            "form": submitted_form})


# def store_files(file):
#     with open(f"tempfiles/{file}", "wb+") as upload:
#         for chunk in file.chunks():
#             upload.write(chunk)
