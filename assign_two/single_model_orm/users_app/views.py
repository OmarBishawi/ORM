from django.shortcuts import render,redirect
from .models import *
# from . import models
# Create your views here.

#To render the index.html & retrieve all data
def index(request):
  context={
      'users':User.get_data(),
      
  }
  return render(request, 'index.html',context)

#handle POST Request from users and  display the data to front-end
def add_user(request):
  if request.method == 'POST':
    User.create_user(request.POST)
    return redirect('/')
  

