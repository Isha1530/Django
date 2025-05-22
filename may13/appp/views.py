from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, World! This is my first Django web application.")

def about(request):
    return render(request, 'about.html')