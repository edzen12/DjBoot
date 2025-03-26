from django import forms 
from .models import Reviews


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1, max_value=5,
        widget=forms.NumberInput(attrs={'type':'number', 'min':'1', 'max':'5'})
    )
    
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'desc', 'rating']