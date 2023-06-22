from django.core.validators import MinLengthValidator
from django.db import models
from .validators import validate_first_letter_is_upper, validate_letters_only

# Create your models here.


"""
Profile Model
"""


class UserProfile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(MinLengthValidator(2),)
    )
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(validate_first_letter_is_upper,)
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(validate_first_letter_is_upper,),
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


"""
Plant model
"""


class Plant(models.Model):
    PLANT_TYPES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants")
    )
    plant_type = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        choices=PLANT_TYPES
    )
    plant_name = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2,),
            validate_letters_only,
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )
