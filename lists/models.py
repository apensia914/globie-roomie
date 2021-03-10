from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):

    ''' List Model Definition ''' 

    name = models.CharField(max_length=80) # Name of the list 
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rooms = models.ManyToManyField('rooms.Room', blank=True) # Rooms within the list 

    def __str__(self):
        return self.name