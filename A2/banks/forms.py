from django import forms
from .models import BankModel



# This form is for  Bank Form
class BankForm(forms.ModelForm):
    class Meta:
        model = BankModel
        fields ='__all__'
        labels = {'name':'Name', 'swift_code':'Swift Code', 'institution_number':'Institution Number', 
                  'description':'Description'}
