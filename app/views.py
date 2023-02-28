from django.shortcuts import render

from app.models import Post
from app.models import Category

# Create your views here.
def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {'posts': posts, 'categories': categories})


def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "post.html", {'post': post})
