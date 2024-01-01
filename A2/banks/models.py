from django.db import models

# Create your models here.
class BankModel(models.Model):
    name = models.CharField(max_length = 100, null=False)
    swift_code = models.CharField(max_length = 100, null= False)
    institution_number = models.CharField(max_length = 100, null=False)
    description = models.CharField(max_length = 100, null=False)


    def __str__(self):
        return self.name