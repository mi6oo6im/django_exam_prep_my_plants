from django.forms import ModelForm
from .models import UserProfile, Plant


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

class BasePlantsForm(ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Plant Type',
            'plant_name': 'Plant Name',
            'image_url': 'Image URL',
        }


class PlantCreate(BasePlantsForm):
    pass


class PlantEdit(BasePlantsForm):
    pass


class PlantDelete(BasePlantsForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
