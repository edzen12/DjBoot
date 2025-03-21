from django.shortcuts import render
from project.models import Course, Books, Settings, Blog


def index(request):
    courses = Course.objects.all()
    settings = Settings.objects.latest('id')
    context = {
        'courses':courses,
        'settings':settings,
    }
    return render(request, 'index.html', context)


def books(request):  
    books = Books.objects.all()
    settings = Settings.objects.latest('id')
    context = {
        'books':books,
        'settings':settings,
    }
    return render(request, 'pages/books.html',context ) 


def book_detail(request, slug):
    settings = Settings.objects.latest('id')
    book = Books.objects.get(slug=slug) 
    context = {
        'settings':settings,
        'book':book, 
    }
    return render(request, 'pages/books-detail.html', context)


def courses(request): 
    courses = Course.objects.all()
    settings = Settings.objects.latest('id')
    context = {
        'courses':courses,
        'settings':settings,
    } 
    return render(request, 'pages/courses.html', context ) 


def blog(request):  
    settings = Settings.objects.latest('id')
    blogs = Blog.objects.all()
    context = { 
        'settings':settings,
        'blogs':blogs,
    } 
    return render(request, 'pages/blog.html',context) 


def blog_detail(request, slug):
    settings = Settings.objects.latest('id')
    blogs_latest = Blog.objects.all()[:3]
    blog = Blog.objects.get(slug=slug) 
    reviews = blog.reviews.all() # получаемые отывы для конкретного поста
    context = {
        'settings':settings,
        'blog':blog, 
        'blogs_latest':blogs_latest, 
        'reviews': reviews, # передача в шаблон
    }
    return render(request, 'pages/blog-detail.html', context)


def contact(request):  
    settings = Settings.objects.latest('id')
    context = { 
        'settings':settings,
    } 
    return render(request, 'pages/contact.html',context) 