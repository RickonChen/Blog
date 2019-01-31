from django.shortcuts import render
from blog.models import Post
# Create your views here.

def home(request):
    items = Post.objects.all()
    return render(request, 'base/home.html', { 'items': items, 'title': 'Home' })