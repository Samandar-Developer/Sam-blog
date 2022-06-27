from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import BlogForm, CommentForm

def home(request):
    return render(request, template_name="pages/index.html")


def blogs(request):
    blogs = Blog.objects.all().filter(is_public=True) 
    context = {
        "blogs": blogs,
    }
    return render(request, template_name="blog/blogs.html", context=context)

@login_required(login_url="user_login")
def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    comment = CommentForm()
    context = {
        "blog":blog,
        "comment":comment,
    }
    return render(request, template_name="blog/blog.html", context=context)

def by_topics(request):
    topics = Theme.objects.all()
    context = {
        "topics":topics,
    }
    return render(request, template_name="pages/by_topics.html", context=context)

def in_topic(request, pk):
    topic = Theme.objects.get(id=pk)
    context = {
        "topic":topic,
    }
    return render(request, "pages/topic.html", context)

def createBlog(request):
    blog = BlogForm()
    if request.method == "POST":
        blog = BlogForm(request.POST, request.FILES)
        if blog.is_valid():
            blog.save()
            return redirect("blogs")

    context = {
        "blog":blog,
    }
    return render(request, template_name="blog/blog_form.html", context=context)


def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog_form = BlogForm(instance=blog)
    if request.method == "POST":
        blog_form = BlogForm(request.POST, request.FILES, instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            return redirect("blogs")
    context = {
        "blog":blog_form,
    }

    return render(request, template_name="blog/blog_form.html", context=context)

def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog_form = BlogForm(instance=blog)
    if request.method == "POST":
        blog.delete()
        return redirect("blogs")

    context = {
        "blog":blog,
    }
    return render(request, template_name="blog/delete.html",context=context)