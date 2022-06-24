from django.urls import path
from . import views


urlpatterns = [
    path("", views.users, name="users"),
    path("login/", views.user_login, name="user_login"),
]