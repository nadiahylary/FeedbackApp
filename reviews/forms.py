from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Username", error_messages={
        "required": "Your username must not be empty!",
        "max_length": "Please enter a shorter name!"
    })
    review = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
