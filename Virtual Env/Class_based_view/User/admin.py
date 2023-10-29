from django.contrib import admin
from .models import Users

# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','is_admin']