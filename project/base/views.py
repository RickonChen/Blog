from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    items = Post.objects.all()
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'base/home.html', { 'items': items, 'title': 'Home' })