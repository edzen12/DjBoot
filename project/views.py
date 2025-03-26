from django.shortcuts import render, redirect
from project.forms import ReviewForm
from project.models import Course, Books, Settings, Blog, Instructors, Reviews


def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = ReviewForm()
    return render(request, 'courses.html', {'form':form})


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


def course_detail(request, slug):
    settings = Settings.objects.latest('id')
    course = Course.objects.get(slug=slug) 
    instructor = Instructors.objects.all()
    context = {
        'settings':settings,
        'course':course, 
        'instructor':instructor, 
    }
    return render(request, 'pages/course-detail.html', context)

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