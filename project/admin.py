from django.contrib import admin

from project.models import (Category, Books, Course, Settings, Blog,
                            SocialLinks, Instructors, Reviews)



class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug']
    prepopulated_fields = {'slug' :('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' :('title',)}


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' :('title',)}

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' :('title',)}

class SocialLinksInline(admin.TabularInline):
    model = SocialLinks
    extra = 1

class InstructorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    inlines = [SocialLinksInline,]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Settings)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(SocialLinks)
admin.site.register(Instructors, InstructorsAdmin)
admin.site.register(Reviews)