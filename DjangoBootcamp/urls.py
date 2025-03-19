
from django.contrib import admin
from django.urls import path, include
from project.views import index, blog, books, contact, courses, book_detail, blog_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='homepage'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('books/', books, name='books'),
    path('books/<slug:slug>/', book_detail, name='book_detail'),
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)