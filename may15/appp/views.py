from django.shortcuts import render
from .models import Category,Product, Student, Register
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

def register(request):
    if request.method == 'POST':
        data = Register()
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.phone_no = request.POST['phone_no']
        data.password = request.POST['password']
        data.confirm_password = request.POST['confirm_password']
        try:
            already_exists = Register.objects.get(email=request.POST["email"])
            if already_exists:
                return render(request, 'register.html', {'error': 'Email already exists'})
        except Register.DoesNotExist:       
            data.save()
            return render(request, 'register.html', {'message': 'Registration successful!'})
        
        if data.password != data.confirm_password:
            return render(request, 'register.html', {'notsame': 'Passwords do not match'})
    
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Register.objects.get(email=email, password=password)
            return render(request, 'login.html', {'message': 'Login successful!'})
        except Register.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')
  