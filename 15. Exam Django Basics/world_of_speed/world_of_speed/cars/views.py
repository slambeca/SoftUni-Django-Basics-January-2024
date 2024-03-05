from django.shortcuts import render, redirect

from world_of_speed.cars.forms import CreateCarForm, EditCarForm, DeleteCarForm
from world_of_speed.cars.models import Car
from world_of_speed.core.utils import get_profile, get_all_cars


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)


def create_car(request):
    profile = get_profile()
    form = CreateCarForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'cars/car-create.html', context)


def catalogue(request):
    profile = get_profile()
    cars = get_all_cars()

    context = {
        'profile': profile,
        'cars': cars,
    }

    return render(request, 'cars/catalogue.html', context)


def details_car(request, car_id):
    car = Car.objects.get(id=car_id)
    profile = get_profile()

    context = {
        'car': car,
        'profile': profile,
    }

    return render(request, 'cars/car-details.html', context)


def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    profile = get_profile()

    form = EditCarForm(instance=car)
    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
        'profile': profile,
    }

    return render(request, 'cars/car-edit.html', context)


def delete_car(request, car_id):
    profile = get_profile()
    car = Car.objects.get(id=car_id)

    form = DeleteCarForm(instance=car)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form,
    }

    return render(request, 'cars/car-delete.html', context)