from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Emp 

# Create your views here.

def emp_home(request):
    emps= Emp.objects.all()   #we have data in models.py and we wanna show that to user , and you know user can see views.py so we are fetching everything here
    return render(request,'emp/home.html',{'emps':emps})  # now we have data from models in our vies.py and now we have to show this data to our user in whicheverway we want, so for that we will use template home.html

def add_emp(request):
    if request.method == 'POST':

        
        # data fetch

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_email = request.POST.get("emp_email")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        
        #validate

        # create model object and set data
        # we create 'e' as an object for class Emp() as we have seen in Advance python classes 
        e=Emp()
        e.name=emp_name # I am getting emp_nme from input tag in add_emp.html so i have to save it in my models.py model Emp so for that I am writing e.name=emp_name
        e.email=emp_email
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        # save the object
        e.save()


        # prepare msg


        return HttpResponseRedirect('/emp/home/')
    return render(request,'emp/add_emp.html/',{})     #for the first time if we are just opening this url then we this url will render this url

def delete_emp(request,emp_id):
    emp= Emp.objects.get(pk=emp_id)
    emp.delete()
    return HttpResponseRedirect('/emp/home/')