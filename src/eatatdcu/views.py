from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   context = {}
   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   context = {}
   return render(request,'eatatdcu/restaurants.html',context)
