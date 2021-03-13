import random
from django_seed import Seed #9.2 
from django.core.management.base import BaseCommand
from reviews.models import Review
from users.models import User 
from rooms.models import Room 

class Command(BaseCommand):
    help = 'Automatically generates many users'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='How many reviews would you like to create?')
        
    #9.2 https://pypi.org/project/django-seed/ 
    #9.6 
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(Review, number, { #9.2 Creating users that are neither staff nor superuser. 
            'accuracy': lambda x: random.randint(0, 5), 
            'communication': lambda x: random.randint(0, 5),
            'cleanliness': lambda x: random.randint(0, 5),
            'location': lambda x: random.randint(0, 5),
            'check_in': lambda x: random.randint(0, 5),
            'value': lambda x: random.randint(0, 5), 
            'room': lambda x: random.choice(rooms),
            'user': lambda x: random.choice(users),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} reviews created!'))