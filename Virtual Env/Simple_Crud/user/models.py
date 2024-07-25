from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    phone_number= PhoneNumberField()
    is_admin= models.BooleanField()

    # class Meta:
    #    verbose_name_plural  = "Categories"
        # ordering = ['-created']
    
    def __str__(self):
        return self.name
    

class Address(models.Model):
    Address=models.TextField()
    # address will automatically delete if user is deleted.
    User=models.ForeignKey(User, on_delete=models.CASCADE, blank=True , null=True)

    def __str__(self):
        return f'{self.Address} |{self.User}'