from django.contrib import admin

from app.models import Post
from app.models import Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
