from django.contrib import admin
from .models import *

# @admin.register()
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "is_public", "date"]
    list_editable = ("is_public",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Theme)
