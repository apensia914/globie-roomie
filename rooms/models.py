from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Field name for RoomType, Amenity and Facility model
class AbstractItem(core_models.TimeStampedModel):

    ''' Abstract Item '''

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True 

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    ''' RoomType Object Definition ''' 

    class Meta:
        verbose_name = 'Room Type'
        verbose_name_plural = 'Room Types' 
        ordering = ['name'] # https://docs.djangoproject.com/en/3.1/ref/models/options/#ordering


class Amenity(AbstractItem):

    ''' Amenity Model Definition ''' 

    # 4.5 
    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities' # https://docs.djangoproject.com/en/3.1/ref/models/options/#verbose-name-plural


class Facility(AbstractItem):

    ''' Facility Model Definition ''' 

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem): # House rules
    
    ''' HouseRule Model Definition ''' 

    class Meta:
        verbose_name = 'House Rule'
        verbose_name_plural = 'House Rules'

class Photo(core_models.TimeStampedModel):
    
    ''' Photo Model Definition '''

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name="photos")

    def __str__(self):
        return self.caption


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
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='rooms') #4.1~4.2 https://docs.djangoproject.com/en/3.1/ref/models/fields/#foreignkey
    room_type = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True, related_name='rooms') #4.3 https://docs.djangoproject.com/en/3.1/ref/models/fields/#manytomanyfield 
    amenities = models.ManyToManyField('Amenity', blank=True, related_name='rooms') #4.4 #7.2
    facilities = models.ManyToManyField('Facility', blank=True, related_name='rooms') #4.4 #7.2
    house_rules = models.ManyToManyField('HouseRule', blank=True, related_name='rooms') #4.4 #7.2 related_name (https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name)

    #4.3 
    def __str__(self):
        return self.name 