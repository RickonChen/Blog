from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models import Post


def search(request):
    q = request.GET.get('q', None)
    items = ''

    if q is None or q is "":
        items = Post.objects.all()
    elif q is not None:
        items = Post.objects.filter(title__contains=q)

    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    title = "Search"

    return render(request, 'search/search.html', { 'items': items, 'title': title })
