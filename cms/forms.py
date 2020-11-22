from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import * 


class ReferrerForm(ModelForm):
    class Meta:
        model = Referrer
        fields = '__all__'
        exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'comments']

class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['full_name', 'email', 'phone']

class AddressForm(ModelForm):
    class Meta:
        model = Delivery_Address
        fields = '__all__'
        exclude = ['recipient']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReferralForm(forms.Form):
    pass