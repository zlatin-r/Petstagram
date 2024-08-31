from django.contrib import admin

from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'location', 'created_at', "short_description", "tagged_pets")

    def tagged_pets(self, obj):
        return ", ".join(pet.name for pet in obj.pets.all())

    def short_description(self, obj):
        return obj.description[:20]
