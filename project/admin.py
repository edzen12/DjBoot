from django.contrib import admin

from project.models import (Category, Books, Course, 
                            SocialLinks, Instructors, Reviews)


admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Course)
admin.site.register(SocialLinks)
admin.site.register(Instructors)
admin.site.register(Reviews)