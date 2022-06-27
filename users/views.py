from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def users(request):
    return render(request, "users/users.html")



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
        except:
            print("User does not exist.")
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print("Password or Username does not match.")
    return render(request, "pages/registration.html")


def user_logout(request):
    logout(request)
    return redirect("home")