from django.contrib import admin

from .models import Student, Document, Courses, Professor, User2

# Register your models here.

admin.site.register(Document)
admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Professor)
admin.site.register(User2)