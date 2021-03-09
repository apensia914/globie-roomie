from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class Room(core_models.TimeStampedModel):

    ''' Room Model Definition '''

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField() #4.1 Django-countries (https://pypi.org/project/django-countries/)
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    instant_book = models.BooleanField(default=False)
    check_in = models.TimeField()
    check_out = models.TimeField()
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE) #4.1~4.2