from django.shortcuts import render
from .models import Page

def home(request):
    return render(request, 'blog_app/home.html')

def about(request):
        return render(request, 'blog_app/about.html')

def pages(request):
    pages = Page.objects.all()
    return render(request, 'blog_app/pages.html', {'pages': pages})

def page_detail(request, page_id):
    page = Page.objects.get(pk=page_id)
    return render(request, 'blog_app/page_detail.html', {'page': page})


