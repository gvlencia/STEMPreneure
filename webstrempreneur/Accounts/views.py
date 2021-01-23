from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect("home")
        else :
            messages.info(request, 'Email or Password is incorrect')

    return render(request, 'page-login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")