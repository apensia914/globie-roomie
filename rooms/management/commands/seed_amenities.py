#9.0 Custom manage.py commands: https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/#module-django.core.management 
from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    help = 'Automatically generates amenities'

    # def add_arguments(self, parser):
    #     parser.add_argument('')
        
    def handle(self, *args, **options):

        amenities = [
            'Air conditioning',
            'Alarm clock',
            'Balcony',
            'Bathroom',
            'Bathtub',
            'Bed linen',
            'Cable TV',
            'Carbon monoxide detectors',
            'Indoor poll',
            'Ironing board',
            'Microwave',
            'Outdoor pool',
            'Outdoor tennis',
            'Oven',
            'Queen size bed',
            'Restaurant',
            'Shopping mall',
            'Shower',
            'Smoke detectors',
            'Sofa',
            'Stereo',
            'Swimming pool',
            'Toilet',
            'Towels',
            'TV',
        ]

        for amenity in amenities: 
            Amenity.objects.create(name=amenity) #9.1 objects has manager to CRUD
        self.stdout.write(self.style.SUCCESS('Amenities created!'))