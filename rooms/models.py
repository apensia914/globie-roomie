from django.db import models
from django.urls import reverse 
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

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
        ordering = ['name'] 


class Amenity(AbstractItem):

    ''' Amenity Model Definition ''' 

    # 4.5 
    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities' 


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
    file = models.ImageField(upload_to='room_photos') 
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name="photos")

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    ''' Room Model Definition '''

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField() 
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
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='rooms') 
    room_type = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True, related_name='rooms') 
    amenities = models.ManyToManyField('Amenity', blank=True, related_name='rooms') 
    facilities = models.ManyToManyField('Facility', blank=True, related_name='rooms') 
    house_rules = models.ManyToManyField('HouseRule', blank=True, related_name='rooms') 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)  
    
    def get_context_data(self, **kwargs):
        return reverse('rooms:detail', kwrags={'pk': self.pk})
    
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0