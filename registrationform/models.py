from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    new_password = models.CharField(max_length=100)
    account_type = models.CharField(max_length=15)  # Assuming a reasonable max length for account type
    terms_and_conditions = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

