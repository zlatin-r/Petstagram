from django.core.exceptions import ValidationError

SIZE_LIMIT = 5 * 1024 * 1024

def validate_file_size(value):
    if value.size > SIZE_LIMIT:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
