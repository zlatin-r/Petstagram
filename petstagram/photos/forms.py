from django import forms

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("photo", "description", "location", "tagged_pets")

class PetPhotoCreateForm(PetPhotoBaseForm):
    pass