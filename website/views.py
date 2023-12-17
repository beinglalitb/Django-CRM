from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Authenticated')
            return redirect('home')
        else:
            messages.error(request, 'There was an error Logging in')
            return redirect('home')
            
    else:
            return render(request, 'home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
     logout(request)
     messages.success(request, "You have been logged out")
     return redirect('home')
 
def register_user(request):
    return render(request, 'register.html', {})
 