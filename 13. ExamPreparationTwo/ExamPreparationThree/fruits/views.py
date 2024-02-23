from django.shortcuts import render, redirect

from ExamPreparationThree.common.helpers import get_profile, get_all_fruits
from ExamPreparationThree.fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from ExamPreparationThree.fruits.models import Fruit


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = get_all_fruits()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'dashboard.html', context)


def add_fruit(request):
    profile = get_profile()
    form = CreateFruitForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, fruit_id):
    profile = get_profile()
    fruit = Fruit.objects.get(id=fruit_id)

    context = {
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = get_profile()

    form = EditFruitForm(instance=fruit)
    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile,
    }

    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = get_profile()

    form = DeleteFruitForm(instance=fruit)

    if request.method == "POST":
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form,
        'profile': profile,
    }

    return render(request, 'fruits/delete-fruit.html', context)