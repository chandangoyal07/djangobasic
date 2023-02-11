from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.

def Home(request):
    return HttpResponse ('<h1>Hello World</h1>')


def About(request):
    cars = Car.objects.all()
    context = {
            'cars': cars
    }
    return render(request,'about.html', context= context)