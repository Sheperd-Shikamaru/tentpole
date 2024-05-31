from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            return redirect('dashboard')
        else:
            context = {
                'email': email,
                'password': password,
                'error': 'Invalid email or password'
            }
            return render(request, 'system_management/login.html', context)

    return render(request, 'system_management/login.html')

def log_out(request):
    logout(request)
    return redirect('landing_page')