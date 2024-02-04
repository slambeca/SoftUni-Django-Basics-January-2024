# Django wants a callable that raises a ValidationError, which also has a single parameter
# Django validators can be function or classes
from django.core.exceptions import ValidationError


def validate_email(email):
    if "@" not in email:
        raise ValidationError("Email is invalid!")


class FileSizeValidator:
    def __int__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        if value.size > self.max_file_size:
            raise ValidationError(f"The size of the file should not exceed {self.max_file_size}!")


validate_email("doncho@minkov.com")
# FileSizeValidator(5)(file)