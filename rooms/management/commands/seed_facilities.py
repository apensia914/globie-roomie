#9.0 Custom manage.py commands: https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/#module-django.core.management 
from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):
    help = 'Automatically generates amenities'

    # def add_arguments(self, parser):
    #     parser.add_argument('')
        
    def handle(self, *args, **options):

        facilities = [
            'Private entrance',
            'Paid parking on premises',
            'Paid parking off premises',
            'Elevator',
            'Parking',
            'Gym'
        ]

        for facility in facilities: 
            Facility.objects.create(name=facility) #9.2 objects has manager to CRUD
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilities created!'))