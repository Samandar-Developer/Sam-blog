from django.forms import ModelForm 
from .models import Blog, Comment

class BlogForm(ModelForm):
    
    class Meta:
        model = Blog
        fields = ("title","cover_image", "description", "topic", "tags", "is_public")


class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ("description","react")
