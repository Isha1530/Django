from django.contrib import admin
from .models import Category,Product,Student
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description' ,'price', 'image')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age','email')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Student, StudentAdmin)