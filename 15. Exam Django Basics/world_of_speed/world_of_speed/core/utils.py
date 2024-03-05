from world_of_speed.cars.models import Car
from world_of_speed.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_all_cars():
    return Car.objects.all() if Car.objects.all() else None


