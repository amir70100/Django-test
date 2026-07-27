from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def login_view(request):

    from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    msg = None
    
    if request.user.is_authenticated:
        msg = f"User is authenticated as {request.user.username}"
        return render(request, 'accounts/login.html', {'msg': msg})
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Please fill all fields!')
            return render(request, 'accounts/login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'accounts/login.html')

def signup_view(request):
    return render(request,'accounts/signup.html')

def logout_view(request):
    pass
