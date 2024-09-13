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














# CBV

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



