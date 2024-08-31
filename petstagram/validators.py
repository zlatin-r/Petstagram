from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

SIZE_5_MB = 5 * 1024 * 1024


def validate_image_size_less_than_5mb(value):
    if value > SIZE_5_MB:
        raise ValidationError("File size should be less than 5MB")


class MaxSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return file_size > max_size
