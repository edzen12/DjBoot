from django import forms 
from django.contrib.auth import get_user_model
from .models import Reviews

User = get_user_model()


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'address', 'gender', 'photo']


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1, max_value=5,
        widget=forms.NumberInput(attrs={'type':'number', 'min':'1', 'max':'5'})
    )
    
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'desc', 'rating']