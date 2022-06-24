from django.shortcuts import render

def users(request):
    return render(request, "users/users.html")



def user_login(request):
    return render(request, "pages/registration.html")