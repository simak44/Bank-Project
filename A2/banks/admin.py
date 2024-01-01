from django.contrib import admin
from .models import BankModel
# Register your models here.
@admin.register(BankModel)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'swift_code', 'institution_number', 'description']