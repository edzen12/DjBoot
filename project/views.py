from django.shortcuts import render
from project.models import Course, Books, Settings


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
    context = { 
        'settings':settings,
    } 
    return render(request, 'pages/blog.html',context) 


def contact(request):  
    settings = Settings.objects.latest('id')
    context = { 
        'settings':settings,
    } 
    return render(request, 'pages/contact.html',context) 