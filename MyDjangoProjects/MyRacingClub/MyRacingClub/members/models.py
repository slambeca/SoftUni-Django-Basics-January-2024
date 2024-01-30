from django.db import models


class Member(models.Model):
    MAX_LENGTH_FIRST_NAME = 255
    MAX_LENGTH_LAST_NAME = 255
    MAX_LENGTH_PHONE = 20

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
    )

    phone = models.CharField(
        max_length=MAX_LENGTH_PHONE,
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )

    car_brand = models.CharField(
        null=True,
        blank=True,
    )

    car_model = models.CharField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"