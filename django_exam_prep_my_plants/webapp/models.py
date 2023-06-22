from django.db import models

# Create your models here.


"""
Profile Model
o	Username
	    Character field, required.
	    It should consist of a maximum of 10 characters.
	    It should consist of a minimum of 2 characters
o	First name
	    Character field, required.
	    It should consist of a maximum of 20 characters.
	    The first name must start with a capital letter. Otherwise raise ValidationError with the following message: "Your name must start with a capital letter!"
o	Last Name
	    Character field, required.
	    It should consist of a maximum of 20 characters.
	    The last name must start with a capital letter. Otherwise raise ValidationError with the following message: "Your name must start with a capital letter!"
o	Profile Picture
	    PURL field, optional.


Plant Model
o	Plant Type
	    Character field, required.
	    It should consist of a maximum of 14 characters.
	    The choices are: "Outdoor Plants" and "Indoor Plants".
o	Name
	    Character field, required.
	    It should consist of a maximum of 20 and a minimum of 2 characters.
	    The name should contain only letters. Otherwise raise a ValidationError with the following message: "Plant name should contain only letters!"
o	Image Url
	    URL field, required.
o	Description
	    Text field, required.
o	Price
	    Float field, required.
"""


class UserProfile(models.Model):
    pass


class Plant(models.Model):
    pass
