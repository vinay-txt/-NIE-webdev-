# for FBV

from django.forms import ModelForm

from .models import Student,Employee

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        
class Employee(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"        


# for login, logout, user registrration
from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
