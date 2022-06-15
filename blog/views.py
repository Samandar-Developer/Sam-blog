from django.shortcuts import render
from .models import Blog


def home(request):
    return render(request, template_name="pages/index.html")


def blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, template_name="blog/blogs.html", context=context)


def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        "blog":blog,
    }
    return render(request, template_name="blog/blog.html", context=context)