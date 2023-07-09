import re
from os import environ

from rest_framework.exceptions import ValidationError


def os_environ_get(value):
    return environ.get(value)


def validate_phone_number(phone):
    pattern = r'^\+998\d{9}$'
    if not re.match(pattern, phone):
        raise ValidationError('Invalid phone number. Please provide a valid phone number in the format of Uzbekistan.')
