from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    MAX_LENGTH = 30

    name = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
    )

    pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        # This didn't work
        # super().save(*args, **kwargs)
        #
        # if not self.slug:
        #     self.slug = slugify(f"{self.name}-{self.pk}")
        #
        # super().save(*args, **kwargs)

        # This work
        # Check if the object is new and slug is not set
        if not self.slug:
            self.slug = slugify(f"{self.name}")
            # Make sure to call the original save method to generate the pk
            super().save(*args, **kwargs)
            # Update the slug with the pk and save again
            self.slug = slugify(f"{self.name}-{self.pk}")
            self.save(update_fields=['slug'])
        else:
            # Call the original save method for existing records
            super().save(*args, **kwargs)
