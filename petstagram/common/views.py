from django.shortcuts import render, redirect
from django.views import generic as views
from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


# def index(request):
#     pet_name_pattern = request.GET.get('pet_name_pattern', '')
#
#     pet_photos = Photo.objects.all()
#
#     if pet_name_pattern:
#         pet_photos = pet_photos.filter(name__icontains=pet_name_pattern)
#
#     context = {
#         "pet_photos": pet_photos,
#         "pet_name_pattern": pet_name_pattern,
#     }
#     return render(request, "common/index.html", context)

class IndexView(views.ListView):
    queryset = Photo.objects.all() \
    .prefetch_related("tagged_pets") \
    .prefetch_related("photolike_set")

    template_name = 'common/index.html'

    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', "")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_name_pattern"] = self.pet_name_pattern
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        if pet_name_pattern:
            filter_query['tagged_pets__name__icontains'] = pet_name_pattern

        return queryset.filter(**filter_query)


def like_pet_photo(request, pk):
    # pet_photo = Photo.objects.get(pk=pk, user=request.user)
    # pet_photo = Photo.objects.get(pk=pk)
    # pet_photo_like = PhotoLike.objects.first(pk=pk, user=request.user)

    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        # dislike
        pet_photo_like.delete()
    else:
        # like
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")
