from django import template

register = template.Library()


# This function won't be available as custom filter in our templates
def say_hello():
    return "Hello, World!"


@register.filter
def only_odd(numbers):
    return [x for x in numbers if x % 2 == 1]


@register.filter
def only_even(numbers):
    return [x for x in numbers if x % 2 == 0]