from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    phone_number= PhoneNumberField()
    is_admin=models.BooleanField()

    def __str__(self):
        return self.name
