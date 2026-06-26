from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Standard Customer Form
class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

# Dedicated Seller Form
class SellerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(required=True, max_length=20)
    home_address = forms.CharField(required=True, max_length=255)
    postal_code = forms.CharField(required=True, max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email']