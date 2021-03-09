from django.db import models

class TimeStampedModel(models.Model):

    ''' Time Stamped Model ''' 

    created = models.DateTimeField(auto_now_add=True) #4.1 Generate new date & time 
    updated = models.DateTimeField(auto_now=True) #4.1 Update with new date & time 

    #4.0: Won't be saved in database
    class Meta: 
        abstract = True
