
from django.contrib import admin
from django.urls import path, include
from project.views import index, blog, books, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='homepage'),
    path('blog/', blog, name='blog'),
    path('books/', books, name='books'),
    path('contact/', contact, name='contact'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)