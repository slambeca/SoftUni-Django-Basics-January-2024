from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.inclusion_tag("tags/profile_avatar.html", takes_context=True)
def show_user(context):
    # Return "context", much like in View's
    # user = User.objects.all().first()
    user = context.request.user
    return {
        "user_fullname": f"{user.first_name} {user.last_name}",
    }