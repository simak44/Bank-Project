from django.db import models
from banks.models import BankModel
from datetime import datetime


# Create your models here.
class BranchModel(models.Model):
    bank_name = models.ForeignKey(BankModel, on_delete=models.CASCADE, null=True)
    branch_name = models.CharField(max_length=100, null = False)
    transit_number = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    email = models.EmailField(default = 'admin@enigmatix.io')
    last_modefied = models.DateTimeField(auto_now = True)
