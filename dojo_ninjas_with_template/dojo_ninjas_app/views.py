from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    dojos = Dojo.objects.all()
    return render(request, 'index.html', {'dojos': dojos})

def add_dojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        Dojo.objects.create(name=name , city= city, state = state)
    return redirect('index')
def add_ninja(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo_id = request.POST['dojo']
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('index')

def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('index')
