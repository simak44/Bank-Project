
from django.contrib import admin
from .models import BranchModel
# Register your models here.
@admin.register(BranchModel)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'bank_name', 'branch_name', 'transit_number', 'address', 'email', 'last_modefied']