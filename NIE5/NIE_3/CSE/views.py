from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    name = 'raju'
    department = 'CSE'
    college_name = 'NIE'
    roll_number = 60145
    context = {'name': name, 'c_name': college_name, 'd_name': department, 'r_number':roll_number}
    return render(request,'products.html', context)

def service(request):
    return render(request,'service.html')

def contacts(request):
    return render(request,'contacts.html')


def basic(request):
    return render(request,'basic.html')

# FBV

from django.shortcuts import render, redirect, get_object_or_404

from CSE.models import Student
from CSE.forms import StudentForm

#Create view

def form(request):
    
    form = StudentForm
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')  

    context = {'form': form}
    return render(request, 'FBV/form.html', context) 



#list view
def student(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request,'FBV/student.html',context)

#detail view
def detail(request, id):
	data = Student.objects.get(id = id)	
	context = {'data':data}
	return render(request,'FBV/detail.html', context)

#Update view
def update(request, id):
	obj = get_object_or_404(Student, id =id)
	form = StudentForm(request.POST or None, instance = obj)
	data = Student.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('CSE:student')

	context = {'form':form, 'data':data}
	return render(request,'FBV/update.html', context )

#delete view

def delete(request, id):
	data = Student.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('CSE:student')
	return render(request,'FBV/delete.html', context )














# CBV-student

from CSE.models import Student
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class StuList(ListView):
    model = Student
    template_name = 'CBV/list.html'


class Forms(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'CBV/forms.html'
    success_url = '/'


class StudentDetail(DetailView):
    model = Student
    template_name = 'CBV/detail.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'CBV/update.html'
    success_url = '/'


class StudentDelete(DeleteView):
    model = Student
    template_name = 'CBV/delete.html'
    success_url = '/'


# CBV-Employee

from CSE.models import Employee
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView    
class EmployeeList(ListView):
    model = Employee
    template_name = 'CBV1/list.html'


class EmpForms(CreateView):
    model = Employee
    fields = "__all__"
    template_name = 'CBV1/forms.html'
    success_url = '/'


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'CBV1/detail.html'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'CBV1/update.html'
    success_url = '/'


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'CBV1/delete.html'
    success_url = '/'



# GET and POST
def nie(request):
	return render(request,'nie.html')


def add(request):
	a = int(request.GET['num1'])
	b = int(request.GET['num2'])
	c = a+b
	context = {'result':c}
	return render(request, 'add.html', context)

def add1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a+b
	context = {'result':c}
	return render(request, 'add.html', context)


# for login, logout, user registration

from django.shortcuts import render, redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 



@login_required(login_url = 'login')
def home(request):
	return render (request,"home.html", context = {})





def register(request):
	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('CSE:login')


	context = { 'form': form }
	return render (request, 'Login/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('CSE:home')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'Login/login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('CSE:login')

