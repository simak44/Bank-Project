from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .forms import UserForm
from django.views.generic.edit import FormView
# Create your views h


# This class is for user creation form
class CreationFormView(FormView):
    form_class = UserForm
    template_name = 'registration/usercreation.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# This class is for Password change 
class PassResetView(FormView):
    form_class = PasswordResetForm
    template_name = 'registration/passreset.html'
    success_url = '/login/' 