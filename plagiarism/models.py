from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class User (models.Model):
#     name=models.CharField(max_length=200)





class User2(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True, null = True)
	user_type = models.CharField(max_length = 100, default = "null", null = True)

	def __str__(self):	
	 return self.user_type

class Courses(models.Model):
	class Meta:
		verbose_name = _('Courses')
	course_Name=models.CharField(max_length=200, default = "null")
	professor=models.ForeignKey("User2", on_delete=models.CASCADE, null = True, blank = True)
	def __str__(self):
	 return self.course_Name

class Student(models.Model):
	class Meta:
		verbose_name = _('Student')
	# user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
	number_documents = models.IntegerField(default = 0)
	number=models.CharField(max_length=200, default = 0)
	course=models.ManyToManyField(Courses, blank = True)
	on_delete = models.CASCADE
	teacher = models.BooleanField(default = False)

	def __str__(self):
		return (self.number)

class User2Inline(admin.StackedInline):
	model = User2
	can_delete = False
	verbose_name_plural = 'TrueUser'

class Professor(models.Model):
	class Meta:
		verbose_name = _('Professor')
	years_teaching = models.IntegerField(default = 0)
	# user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)

class ProfessorInline(admin.StackedInline):
	model = Professor
	can_delete = False
	verbose_name_plural = 'Professor'


class User2Admin(BaseUserAdmin):
	inlines = (User2Inline,)

class Document(models.Model):
	title = models.CharField(max_length=200, default=".")
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	sub_date = models.DateTimeField(auto_now_add=True)
	document = models.FileField(upload_to='documents/', null=True)
	course=models.ForeignKey(Courses, null=True, on_delete=models.CASCADE)
	keywords=models.CharField(max_length=500, null=True)
	on_delete = models.CASCADE
	approved = models.BooleanField(default = False)
	evaluator = models.ForeignKey('User2', on_delete=models.CASCADE, null = True, blank = True)


	def __str__(self):
		return(self.title)

admin.site.unregister(User)
admin.site.register(User, User2Admin)


