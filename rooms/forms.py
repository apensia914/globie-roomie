from django import forms
from django_countries.widgets import CountryField #13.8
from . import models

class SearchForm(forms.Form):
    
    city = forms.CharField(initial='Anywhere')
    country = CountryField(default='KR').formfield() #13.8
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(required=False, empty_label='Any Kind', queryset=models.RoomType.objects.all()) #13.7 ModelChoiceField
    guests = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(queryset=models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple)
    facilities = forms.ModelMultipleChoiceField(queryset=models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple)


    '''
    ** Documentation URL Link
    #13.7 ModelChoiceField: https://docs.djangoproject.com/en/3.1/ref/forms/fields/#django.forms.ModelChoiceField
    '''