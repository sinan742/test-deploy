from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student

def index(request):
    students = Student.stud.filter()

    first = int(request.GET.get('num1'))
    second = int(request.GET.get('num2'))

    data ={
        'sum':first + second,
        'min':first - second,
        'square':first * second,
    }
        
    return JsonResponse(data,safe=False)