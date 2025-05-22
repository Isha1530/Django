from django.contrib import admin
from .models import register
# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'password', 'confirm_password')
admin.site.register(register, RegisterAdmin)