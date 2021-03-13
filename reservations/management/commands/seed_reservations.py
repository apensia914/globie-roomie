import random
from datetime import datetime, timedelta #9.8
from django_seed import Seed #9.2 
from django.core.management.base import BaseCommand
from reservations.models import Reservation
from users.models import User 
from rooms.models import Room 

class Command(BaseCommand):
    help = 'Automatically generates many reservations'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='How many reservations would you like to create?')
        
    #9.2 https://pypi.org/project/django-seed/ 
    #9.8 
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(Reservation, number, { #9.2 Creating users that are neither staff nor superuser. 
            'guests': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms),
            'check_in': lambda x: datetime.now(),
            'check_out': lambda x: datetime.now() + timedelta(days=random.randint(3, 25))
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} reservations created!'))