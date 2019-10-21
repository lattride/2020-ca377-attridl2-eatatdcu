from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Campus
import json, requests

def index(request):
   context = {}
   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   campus_name = request.GET.get('campus').lower()

   try:
      # retrieve the campus id from the db given this campus name
      campus = Campus.objects.get(name=campus_name)
      # find all restaurants for that campus 
      restaurants = Restaurant.objects.filter(campus_id=campus)
      # put the information returned from the db in the context dictionary
      context = {'restaurants':restaurants}
   except Campus.DoesNotExist:
      # handles the case where an invalid campus name is entered
      context = {'error':'No such campus'}

   return render(request,'eatatdcu/restaurants.html',context)

def specials(request,restaurant):
    webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restaurant
    spec = requests.get(url=webservice_url)
    data = spec.json()
    context = {'daily_special':data}
    
    return render(request,'eatatdcu/specials.html',context)
    # call the web service to get the daily special for "restaurant"
    # pass the information returned by the web service into the "specials.html" template using render function
