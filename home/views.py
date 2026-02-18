from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    students = Student.stud.reverse()
        
    return render(request,'home.html',{'item':students})