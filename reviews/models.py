from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=100)
    review = models.TextField(max_length=1000)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])





