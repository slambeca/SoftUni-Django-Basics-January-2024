import random

from django.shortcuts import render

car_images = (
    "https://www.motortrend.com/uploads/2022/10/2023-BMW-M5-exterior-8.jpg",
    "https://hips.hearstapps.com/hmg-prod/images/2024-bmw-m3-110-1674509061.jpg"
    "?crop=0.732xw:0.548xh;0.0833xw,0.305xh&resize=1200:*",
)

car_names = (
    "M5 Competition xDrive",
    "M3 Competition xDrive",
    "Veyron",
)


def index(request):
    index = random.randint(0, len(car_images) - 1)
    context = {
        "car_image": car_images[index],
        "car_name": car_names[index],
        "numbers": [x + 1 for x in range(20)],
    }
    return render(request, "web/index.html", context)


def about(request):
    return render(request, "web/about.html")