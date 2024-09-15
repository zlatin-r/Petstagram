from django.contrib import admin

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id","date_of_publication", "description", "location", "get_tagged_pets")

    def get_tagged_pets(self, obj):
        return ", ".join([pet.name for pet in obj.tagged_pets.all()])
