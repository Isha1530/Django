from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Distributor
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout


# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('c_password')
        phone = request.POST.get('phone')


        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif Distributor.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
        else:
            user = Distributor(username=username, email=email, phone=phone, password=make_password(password))
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Distributor.objects.get(email=email)
            if check_password(password, user.password):
                request.session['email'] = user.email
                messages.success(request, 'Login successful!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid password.')
        except Distributor.DoesNotExist:
            messages.error(request, 'User does not exist.')
    return render(request, 'login.html')

def user_logout(request):
    if 'email' in request.session:
        del request.session['email']
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('login')


def profile(request):
    email = request.session.get('email')
    if not email:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('login')

    distributor = Distributor.objects.get(email=email)

    if request.method == 'POST':
        distributor.username = request.POST.get('username')
        distributor.email = request.POST.get('email')
        distributor.phone = request.POST.get('phone')

        password = request.POST.get('password')
        if password:
            distributor.password = make_password(password)

        distributor.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('profile')

    return render(request, 'profile.html', {'distributor': distributor})
