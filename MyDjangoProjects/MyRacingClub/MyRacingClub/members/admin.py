from django.contrib import admin

from MyRacingClub.members.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "date_joined",
    )