from django.core.validators import MinValueValidator
from django.db import models

from ExamPreparationFour.profiles.models import Profile


class Genre(models.TextChoices):
    GENRE_POP = 'Pop Music'
    GENRE_JAZZ = 'Jazz Music'
    GENRE_ROCK = 'Rock Music'
    GENRE_COUNTRY = 'Country Music'
    GENRE_RNB = 'R&B Music'
    GENRE_DANCE = 'Dance Music'
    GENRE_HIP_HOP = 'Hip Hop Music'
    GENRE_OTHER = 'Other'


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    # GENRE_POP_MUSIC = 'Pop Music'
    # GENRE_JAZZ_MUSIC = 'Jazz Music'
    # GENRE_ROCK_MUSIC = 'Rock Music'
    # GENRE_COUNTRY_MUSIC = 'Country Music'
    # GENRE_RNB_MUSIC = 'R&B Music'
    # GENRE_DANCE_MUSIC = 'Dance Music'
    # GENRE_HIP_HOP_MUSIC = 'Hip Hop Music'
    # GENRE_OTHER_MUSIC = 'Other'
    #
    # GENRES = (
    #     (GENRE_POP_MUSIC, GENRE_POP_MUSIC),
    #     (GENRE_JAZZ_MUSIC, GENRE_JAZZ_MUSIC),
    #     (GENRE_ROCK_MUSIC, GENRE_ROCK_MUSIC),
    #     (GENRE_COUNTRY_MUSIC, GENRE_COUNTRY_MUSIC),
    #     (GENRE_RNB_MUSIC, GENRE_RNB_MUSIC),
    #     (GENRE_DANCE_MUSIC, GENRE_DANCE_MUSIC),
    #     (GENRE_HIP_HOP_MUSIC, GENRE_HIP_HOP_MUSIC),
    #     (GENRE_OTHER_MUSIC, GENRE_OTHER_MUSIC),
    # )

    MIN_PRICE = 0.0

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )

    artist_name = models.CharField(    # I have used artist_name and not artist for lesser confusion
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name='Artist',
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=Genre.choices,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

    owner = models.ForeignKey(
        Profile,
        # TODO: Check owner foreign key
        on_delete=models.CASCADE,
    )