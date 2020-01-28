# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Car


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    cars = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', { 'car': cars })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = ['description', 'year']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'