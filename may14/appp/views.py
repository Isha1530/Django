from django.shortcuts import render
from .models import Category,Product, Student
# Create your views here.

def index(request):
    return render(request, 'index.html')

def table(request):
    categories = Category.objects.all()
    print(categories)
    # for category in categories:
    #     print(category.id)
    #     print(category.name)
    #     print(category.image)
    products = Product.objects.all()
    print(products)

    student = Student.objects.all()
    print(student)
    return render(request, 'table.html',{'student': student} )

def student_data(request):
    if(request.method == 'POST' and request.FILES):
        # student_data = Student()
        # student_data.name = request.POST['name']
        # student_data.email = request.POST['email']
        # student_data.age = request.POST['age']
        # student_data.save()
        # student_data = Category()
        # student_data.name = request.POST['name']
        # student_data.image = request.FILES['image']
        # student_data.save()
        data = Product()
        data.name = request.POST['name']
        data.description = request.POST['description']
        data.price = request.POST['price']
        data.image = request.FILES['image']
        data.save()
    return render(request,'student.html')