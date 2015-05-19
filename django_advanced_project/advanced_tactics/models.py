from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField


class Hobby(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User)

    # The additional attributes will include.
    birthdate = models.DateField(blank=True)

    HAIR_COLOR_CHOICES = (
        ('BLACK', 'Black'),
        ('BROWN', 'Brown'),
        ('RED', 'Red'),
        ('BLONDE', 'Blonde'),
        ('SALTNPEPPER', 'Salt N Peppa'),
        ('GREEN', 'Green'),
    )

    hair_color = models.CharField(max_length=128,
                                    choices=HAIR_COLOR_CHOICES,
                                    blank=True)

    favorite_hobby = models.ForeignKey(Hobby)

    created = models.DateTimeField(default=datetime.now())

    phone = PhoneNumberField(null=False, default="XXX-XXX-XXXX")

    city = models.CharField(max_length=60, default='San Francisco')

    state = USStateField(blank=True)

    zipcode = USZipCodeField(blank=True)

    def __unicode__(self):
        return self.user.username
