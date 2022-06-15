from django.db import models
import uuid 


class Blog(models.Model):
    # owner
    title = models.CharField(max_length=200) 
    cover_image = models.ImageField(default="default.jpg", null=True, blank=True, upload_to="cover_img/")
    description = models.TextField(null=True, blank=True)
    topic = models.ForeignKey("Theme", on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    is_public = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title
    


class Tag(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    GOOD="Good"
    BAD="Bad"
    EMOJI_TYPE = (
        (GOOD, "👍"),
        (BAD, "👎")
    )
    # owner 
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    react = models.CharField(max_length=100, choices=EMOJI_TYPE, default=GOOD, null=True, blank=True)

    def __str__(self):
        return self.react
    
class Theme(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title
    