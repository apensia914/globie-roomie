from django.contrib import admin
from django.utils.html import mark_safe 
from . import models

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule) #4.4
class ItemAdmin(admin.ModelAdmin):

    ''' Item Admin Definition ''' 

    list_display = ( 
        'name',
        'used_by',
    )

    def used_by(self, obj):
        return obj.rooms.count()

class PhotoInline(admin.TabularInline): 
    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    ''' Room Admin Definition ''' 

    inlines = (PhotoInline,) 

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
        'count_photos', 
        'total_rating', 
    )

    list_filter = (
        'city', 
        'country', 
        'instant_book', 
        'room_type', 
        'amenities', 
        'facilities', 
        'house_rules', 
        'host__superhost', 
        'host__gender', 
    ) 

    raw_id_fields = ('host',) 
    search_fields = ['city', 'host__username'] 
    filter_horizontal = ['amenities', 'facilities', 'house_rules'] 
    ordering = ('name', 'price', 'bedrooms') 
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

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

    list_display = (
        '__str__',
        'get_thumbnail',
    ) 

    def get_thumbnail(self, obj): 
        return mark_safe(f'<img width="150px" src="{obj.file.url}" />') 
    get_thumbnail.short_description = 'Thumbnail'