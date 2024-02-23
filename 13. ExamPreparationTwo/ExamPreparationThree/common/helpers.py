from ExamPreparationThree.fruits.models import Fruit
from ExamPreparationThree.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_all_fruits():
    return Fruit.objects.all() if Fruit.objects.all() else None