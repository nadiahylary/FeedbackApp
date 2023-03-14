from django import forms

from reviews.models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100, label="Username", error_messages={
#         "required": "Your username must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ["username", "review", "rating"]
        # exclude = ["field_to_be_excluded"]
        labels = {
            "username": "User name",
            "review": "Review",
            "rating": "Your Rating"
        }
        error_messages = {
            "username": {
                "max_length": "Please enter a shorter username",
                "required": "This field is required"
            }
        }

