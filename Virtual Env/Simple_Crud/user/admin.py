from django.contrib import admin
from .models import User,Address

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ['name', 'phone_number','is_admin']
    
class AdminAddress(admin.ModelAdmin):
    list_display=['Address','User']

admin.site.register(User,AdminUser)
admin.site.register(Address, AdminAddress)