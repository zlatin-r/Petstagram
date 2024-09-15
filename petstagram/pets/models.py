from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Pet(models.Model):
    MAX_PET_PHOTO_LENGTH = 500

    name = models.CharField(
        max_length=30
    )
    pet_photo = models.URLField(
        null=False,
        blank=True,
        max_length=MAX_PET_PHOTO_LENGTH
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
