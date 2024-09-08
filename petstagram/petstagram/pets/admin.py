from django.contrib import admin

from petstagram.pets.models import Pet

# admin.site.register(Pet)  <- Other way to register models in the admin panel (not recommended)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'slug')
