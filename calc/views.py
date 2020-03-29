from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'vinay jawadwar'})

def add(request):
    val1 = int(request.POST['num1'])                  #we are using POST instead of GET to hide num1 & num2 in address bar
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request,"result.html",{"result":res})