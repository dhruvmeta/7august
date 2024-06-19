from django.shortcuts import render

# Create your views here.

def singup (request):
    return render (request,'singup.html')

def login (request):
    return render (request,'login.html')



