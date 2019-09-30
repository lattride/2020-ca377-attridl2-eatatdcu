from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Campus

def index(request):
   context = {}
   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   context = {}

   #TODO get the campus name from the request
   campus_name = request.GET.get('campus').lower()

   #TODO retrieve the campus id from the db given this campus name
   #TODO find all restaurants for that campus 
   #
   try:
       campus = Campus.objects.get(name=campus_name)
       restaurants = Restaurant.objects.filter(campus_id=campus)
       context = {'restaurants':restaurants}
   except Restaurant.DoesNotExist:
       context = {'error':'No such restaurant'}
   except Campus.DoesNotExist:
       context = {'error':'No such campus'}

   return render(request,'eatatdcu/restaurants.html',context)
