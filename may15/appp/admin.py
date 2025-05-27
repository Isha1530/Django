from django.contrib import admin
from .models import Category,Product,Student,Register
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description' ,'price', 'image')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age','email')

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_no', 'password', 'confirm_password')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Student, StudentAdmin)

admin.site.register(Register, RegisterAdmin)