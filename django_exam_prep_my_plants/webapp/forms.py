from django.forms import ModelForm
from .models import UserProfile


# manage profile forms

class BaseProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class ProfileCreate(BaseProfileForm):
    pass


class ProfileEdit(BaseProfileForm):
    BaseProfileForm.Meta.fields.append('profile_picture')


# manage plants forms
class PlantCreate(ModelForm):
    class Meta:
        pass


class PlantEdit(ModelForm):
    class Meta:
        pass


class PlantDelete(ModelForm):
    class Meta:
        pass
