# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager

# # Use this option if you are happy with the existing fields on the user model and just want to remove the username field.
# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
    
#----------------------------------------------------------------------------------------------
    
# Use this option if you want to start from scratch by creating your own, completely new user model.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
