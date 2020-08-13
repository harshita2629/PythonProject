from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request,'accounts/dashboard.html')

def Services(request):
    return HttpResponse('Different Services')

def Login(request):
    return HttpResponse('Please Login')