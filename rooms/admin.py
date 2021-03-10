from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule) #4.4
class ItemAdmin(admin.ModelAdmin):

    ''' Item Admin Definition ''' 

    list_display = ( #7.3
        'name',
        'used_by',
    )

    def used_by(self, obj): #7.3
        return obj.rooms.count()

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    ''' Room Admin Definition ''' 

    fieldsets = (
        (
            'Basic Info', 
            {"fields": ('name', 'description', 'country', 'address', 'price')}
        ),
        (
            'Times',
            {'fields': ('check_in', 'check_out', 'instant_book')}
        ),
        (
            'More About the Space', 
            {'classes': ('collapse',),
            'fields': ('amenities', 'facilities', 'house_rules')}
        ),
        (
            'Spaces',
            {'fields': ('guests', 'bedrooms', 'beds', 'baths')}
        ),
        (
            'Last Details',
            {'fields': ('host',)}
        ),
    )
    

    list_display = (
        'name',
        'country',
        'city',
        'price',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'count_amenities',
        'count_photos', #7.3
    )

    list_filter = (
        'city', 
        'country', 
        'instant_book', 
        'room_type', 
        'amenities', 
        'facilities', 
        'house_rules', 
        'host__superhost', #6.1 Can add filter from different models
        'host__gender', #6.1 Can add filter from different models
    ) 

    search_fields = ['city', 'host__username'] #6.0 Search-bar in admin (https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
    filter_horizontal = ['amenities', 'facilities', 'house_rules'] #6.1 Applies to ManyToMany Relationships (https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal)
    ordering = ('name', 'price', 'bedrooms') #6.2 https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.ordering

    #6.2 Custom admin function: returning number of amenities
    def count_amenities(self, obj):
        return obj.amenities.count()
    count_amenities.short_description = '# of amenities'

    #7.3 Custom admin function: returning number of photos
    def count_photos(self, obj):
        return obj.photos.count()

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    ''' Photo Admin Definition ''' 

    pass 