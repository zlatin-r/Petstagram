from django.urls import path, include

from petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailView, PetPhotoEditView

urlpatterns = (
    path("add/", PetPhotoCreateView.as_view(), name="add photo"),
    path("<int:pk>/",
         include([
             path("", PetPhotoDetailView.as_view(), name="details photo"),
             path("edit/", PetPhotoEditView.as_view(), name="edit photo"),
         ]))
)
