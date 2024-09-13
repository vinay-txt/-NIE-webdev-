from django.contrib import admin

# Register your models here.
from CSE.models  import Student,Employee

admin.site.register(Student)
admin.site.register(Employee)
