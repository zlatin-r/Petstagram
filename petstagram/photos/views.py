from django.urls import reverse

from django.shortcuts import render
from django.views import generic as view

from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import Photo


class PetPhotoCreateView(view.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/photo-add-page.html"
    queryset = Photo.objects.all() \
        .prefetch_related("tagged_pets")

    def get_success_url(self):
        return reverse("details photo", kwargs={"pk": self.object.pk})


# def add_photo(request):
#     pets = Pet.objects.all()  # Fetch all pets from the database
#     context = {
#         'pets': pets,
#     }
#     return render(request, "photos/photo-add-page.html", context)


class PetPhotoDetailView(view.DetailView):
    queryset = Photo.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("comment_set") \
        .prefetch_related("tagged_pets")

    template_name = "photos/photo-details-page.html"


# def details_photo(request, pk):
#     context = {
#         "pet_photo": Photo.objects.get(pk=pk),
#     }
#     return render(request, "photos/photo-details-page.html", context)


class PetPhotoEditView(view.UpdateView):
    queryset = Photo.objects.all() \
        .prefetch_related("tagged_pets")
    template_name = "photos/photo-edit-page.html"
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse("details photo", kwargs={"pk": self.object.pk})

# def edit_photo(request, pk):
#     return render(request, "photos/photo-edit-page.html")
