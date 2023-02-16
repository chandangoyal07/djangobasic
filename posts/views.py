from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
import datetime
# Create your views here.

def Homego(request):
    return HttpResponse ('<h1>Hello MyWorld3.0</h1>')


def About(request):
    cars = Car.objects.all()
    context = {
            'cars': cars
    }
    return render(request,'about.html', context= context)

def Aboutus(request):
    return render(request,'aboutus.html',{})

def Services(request):
    return render(request,'services.html',{})

def Home(request):
    isActive = True 
    if request.method == 'POST':
        # check=request.POST['check']
        check=request.POST.get('check')  
        print(check)
        if check is None: isActive=False
        else: isActive=True


    mar = datetime.datetime.now()

    name='Goyal_chandan'
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime numbers',
        'WAP to print all prime numbers between 1 tp 100',
        'WAP to print pascals triangle'
    ]

    student={
        'student_name':'rahul',
        'student_college':'GLAU',
        'student_city':'Vridavan',
    }

    data={
        'date':mar,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,'home.html',data)