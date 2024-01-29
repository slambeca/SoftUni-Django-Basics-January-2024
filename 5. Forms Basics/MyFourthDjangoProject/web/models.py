from django.db import models


class Employee(models.Model):
    MAX_FIRST_NAME_LENGTH = 35
    MAX_LAST_NAME_LENGTH = 35

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=False,    # It is by default like this, but also a good practice to add them
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"The full name of this employee is {self.first_name} {self.last_name}"