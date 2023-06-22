from django.core.exceptions import ValidationError


def validate_first_letter_is_upper(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')
