from django.shortcuts import render

from app.models import Post
from app.models import Category

# Create your views here.
def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {'posts': posts, 'categories': categories})