from django.urls import path 
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<str:pk>", views.blog, name="blog"),
    path("topics/", views.by_topics, name="by_topics"),
    path("create_blog/", views.createBlog, name="create_blog"),
    path("update/<str:pk>", views.updateBlog, name="update_blog"),
    path("delete/<str:pk>", views.deleteBlog, name="delete_blog"),
]
