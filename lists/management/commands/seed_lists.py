import random
from django_seed import Seed #9.2 
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from lists.models import List
from users.models import User 
from rooms.models import Room 

class Command(BaseCommand):
    help = 'Automatically generates many lists'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='How many lists would you like to create?')
        
    #9.2 https://pypi.org/project/django-seed/ 
    #9.7 
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all() #9.7 Limiting arrays (4:06)
        seeder.add_entity(List, number, { #9.2 Creating users that are neither staff nor superuser. 
            'user': lambda x: random.choice(users),
        })
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add) #9.7 We want elements of array inside, not querysets. 
            
        self.stdout.write(self.style.SUCCESS(f'{number} of lists created!'))