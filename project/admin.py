from django.contrib import admin

from project.models import (Category, Books, Course, 
                            SocialLinks, Instructors, Reviews)



class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug']
    prepopulated_fields = {'slug' :('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' :('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Course)
admin.site.register(SocialLinks)
admin.site.register(Instructors)
admin.site.register(Reviews)