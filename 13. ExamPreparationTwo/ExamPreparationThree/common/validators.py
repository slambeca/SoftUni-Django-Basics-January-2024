from django.core.exceptions import ValidationError


def validate_name(some_name):
    if not some_name[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def validate_fruit_name(fruit_name):
    if not fruit_name.isalpha():
        raise ValidationError('Fruit name should contain only letters!')