from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Campus
import json,requests

def index(request):
   context = {}
   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   context = {}

   # get the campus name from the request
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

    # call the web service to get the daily special for "restaurant"
    real_time_info = requests.get(webservice_url).json()

    # pass the information returned by the web service into the "specials.html" template using render function
    return render(request,'eatatdcu/specials.html',real_time_info)

