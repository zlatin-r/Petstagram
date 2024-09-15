from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    pets = Pet.objects.all()  # Fetch all pets from the database
    context = {
        'pets': pets,
    }
    return render(request, "photos/photo-add-page.html", context)


def details_photo(request, pk):
    context = {
        "pet_photo": Photo.objects.get(pk=pk),
    }
    return render(request, "photos/photo-details-page.html", context)


def edit_photo(request, pk):
    return render(request, "photos/photo-edit-page.html")



