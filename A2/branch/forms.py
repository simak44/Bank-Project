from django import forms
from .models import BranchModel

# This class is for branch forms
class BranchForm(forms.ModelForm):
    class Meta:
        model = BranchModel
        fields = '__all__'
        labels = {'bank_name':'Bank Name', 'branch_name':'Branch Name', 'transit_number':'Transit Number', 
                  'address':'Address', 'email':'Email'}
        # exclude = ['last_modefied']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }