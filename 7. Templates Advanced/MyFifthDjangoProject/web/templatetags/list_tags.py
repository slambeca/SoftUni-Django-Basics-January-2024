import datetime

from django import template

register = template.Library()


@register.simple_tag
def list_of(values):
    items_string = [f"<li>{value}</li>" for value in values]
    return f"<ul>{items_string}</ul>"


@register.simple_tag()
def current_time():
    return datetime.datetime.now()