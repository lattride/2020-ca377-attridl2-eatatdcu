from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
   context = {}
   return render(request,'eatatdcu/index.html',context)

# TODO add a restaurants function which loads the restaurants.html template
