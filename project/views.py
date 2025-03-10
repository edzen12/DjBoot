from django.shortcuts import render
from project.models import Course, Books


def index(request):
    courses = Course.objects.all()
    context = {
        'courses':courses,
    }
    return render(request, 'index.html', context)


def books(request):  
    books = Books.objects.all()
    context = {
        'books':books,
    }
    return render(request, 'pages/books.html',context ) 


def blog(request):  
    return render(request, 'pages/blog.html' ) 


def contact(request):  
    return render(request, 'pages/contact.html' ) 