# Create your views here.
from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Car
from .forms import MaintenanceForm

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
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', {
        'car': cars, 'maintenance_form': maintenance_form
    })

def add_maintenance(request, car_id):
    # create the ModelForm using the data in request.POST
    form = MaintenanceForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the car_id assigned
        new_maintenance = form.save(commit=False)
        new_maintenance.car_id = car_id
        new_maintenance.save()
    return redirect('detail', car_id=car_id)


class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = ['description', 'year']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'