from django.core import validators
from django import forms
from .models import Review


class ReviewForm (forms.ModelForm):
    nik_name = forms.CharField(required=True, 
        validators=[
            validators.MinLengthValidator(3), 
            validators.MaxLengthValidator(30)
        ])
    
    email = forms.EmailField(required=True)

    stars = forms.IntegerField(required=True, 
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5)
        ])
    
    description = forms.CharField(required=True, 
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(250)
        ])
    

    class Meta:
        model = Review
        fields = ["nik_name", "email", "stars", "description"]