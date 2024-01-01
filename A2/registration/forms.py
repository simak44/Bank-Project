from django import forms
from django.contrib.auth.models import User


# This modelform is for User 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',]
        widgets = { 'password' : forms.PasswordInput, 
                   'email': forms.EmailInput}