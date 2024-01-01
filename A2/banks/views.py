from typing import Any
from django.shortcuts import render
from .models import BankModel
from branch.models import BranchModel
from .forms import BankForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


# This class is for Home View
class HomeView(TemplateView):
    template_name = 'banks/home.html'

# This class is for first Home View
class MyHomeView(TemplateView):
    template_name = 'banks/myhome.html'
 

#  This class is for Bank Form View
class BankFormView(FormView):
    form_class = BankForm
    template_name = 'banks/bankform.html'
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save()
        
        return super().form_valid(form)


# This View is for Dashboard
class DashboardView(TemplateView):
    template_name = 'banks/dashboard.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        bnk = BankModel.objects.all()
        brnh = BranchModel.objects.all()
        context = {'bank':bnk, 'branch':brnh }
        return context
    
# This view is for Update Bank
class BankUpdateview(SuccessMessageMixin, UpdateView):
    model = BankModel
    fields = ['name', 'swift_code', 'institution_number', 'description']
    success_url = '/dashboard/'
    success_message = 'Bank Updates Successfully'
    template_name = 'banks/bankform.html'

# This View is for Delete Bank
class BankDeleteView(DeleteView):
    model = BankModel
    success_url = '/dashboard/'
