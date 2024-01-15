from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=120,
    )

    description = models.TextField()

    is_completed = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description {self.description}")