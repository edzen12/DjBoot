
from django.contrib import admin
from django.urls import path, include
from project.views import (index, blog, books, contact, courses, 
                           book_detail, blog_detail, course_detail, 
                           submit_review, login_view, reg_view, 
                           logout_view, profile_view)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', reg_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'), 
    path('', index, name='homepage'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('books/', books, name='books'),
    path('books/<slug:slug>/', book_detail, name='book_detail'),
    path('courses/', courses, name='courses'),
    path('course/<slug:slug>/', course_detail, name='course_detail'),
    path('contact/', contact, name='contact'),
    path('submit-review/', submit_review, name='submit_review')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)