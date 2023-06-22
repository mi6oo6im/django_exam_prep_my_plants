from django import template

from django_exam_prep_my_plants.webapp.models import UserProfile

register = template.Library()


@register.simple_tag
def get_profile_object():
    profile = UserProfile.objects.first()
    return profile
