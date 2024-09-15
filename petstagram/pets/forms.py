from django import forms
from petstagram.core.forms_mixins import ReadOnlyFieldFormMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = ("name", "date_of_birth", "pet_photo",)

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Pet name'}),
            "date_of_birth": forms.DateInput(attrs={'type': 'date'}),
            "pet_photo": forms.URLInput(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            "name": "Pet name",
            "pet_photo": "Link to image",
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(ReadOnlyFieldFormMixin, PetBaseForm):
    readonly_fields = ("date_of_birth",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

        self.fields["date_of_birth"].widget.attrs["readonly"] = "readonly"

    def clean_date_of_birth(self):  # Validate date_of_birth. Cant be edited true the HTML

        # date_of_birth = self.cleaned_data["date_of_birth"]
        #
        # if date_of_birth != self.instance.date_of_birth:
        #     raise ValidationError("Date of birth is readonly")
        # return date_of_birth

        return self.instance.date_of_birth  # returns every time the true date of birth


class PetDeleteForm(ReadOnlyFieldFormMixin, PetBaseForm):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            # self.instance.comment.delete()
            # self.instance.like.delete()
            self.instance.delete()

        return self.instance
