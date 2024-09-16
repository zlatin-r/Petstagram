from django import forms

from petstagram.core.forms_mixins import ReadOnlyFieldFormMixin
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("photo", "description", "location", "tagged_pets")


class PetPhotoCreateForm(PetPhotoBaseForm):
    pass


class PetPhotoEditForm(ReadOnlyFieldFormMixin, PetPhotoBaseForm):
    readonly_fields = ("photo",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()
