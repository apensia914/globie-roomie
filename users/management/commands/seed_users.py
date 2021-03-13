from django_seed import Seed #9.2 
from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Automatically generates many users'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='How many users would you like to create?')
        
    #9.2 https://pypi.org/project/django-seed/ 
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number, { #9.2 Creating users that are neither staff nor superuser. 
            'is_staff': False,
            'is_superuser': False
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))