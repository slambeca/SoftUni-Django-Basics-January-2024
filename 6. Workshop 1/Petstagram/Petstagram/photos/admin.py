from django.contrib import admin

from Petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass