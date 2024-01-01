from django.shortcuts import render
from .models import BranchModel
from banks.models import BankModel
from .forms import BranchForm
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django import forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
# This class is for Home View
class HomeView(TemplateView):
    template_name = 'banks/home.html'

#  This class is for Bank Form View
class BranchFormView(FormView):
    form_class = BranchForm
    template_name = 'branch/branchform.html'
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# This view is for dashboard
class BranchDashboardView(TemplateView):
    template_name = 'banks/dashboard.html'

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        brnh = BranchModel.objects.all()
        bnk = BankModel.objects.all()
        context = {'branch':brnh, 'bank':bnk}
        return context
    
# This view is for Update Branch
class BranchUpdateview(SuccessMessageMixin, UpdateView):
    model = BranchModel
    fields = ['bank_name', 'branch_name', 'transit_number', 'address', 'email']
    success_url = '/dashboard/'
    success_message = 'Branch Updates Successfully'
    template_name = 'branch/branchform.html'

    def get_form(self):
        form =  super().get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'readonly': 'readonly'})
        return form

# This View is for Delete Bank
class BranchDeleteView(DeleteView):
    model = BranchModel
    success_url = '/dashboard/'