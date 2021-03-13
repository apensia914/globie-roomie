import random
from django_seed import Seed #9.2 
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from users.models import User
from rooms.models import Room, RoomType, Photo, Amenity, Facility, HouseRule

class Command(BaseCommand):
    help = 'Automatically generates many rooms'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=2, type=int, help='How many rooms would you like to create?')
        
    #9.2 https://pypi.org/project/django-seed/ 
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        all_users = User.objects.all() #9.3 Importing all users to create rooms associated. Not recommended to use this when data is too big. 
        room_types = RoomType.objects.all() #9.3 Error: room_type error 
        #9.5 Including amenities, facilities and rules
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        rules = HouseRule.objects.all() 

        seeder.add_entity(Room, number, { #9.2 Creating users that are neither staff nor superuser. 
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(room_types),
            #9.3 Avoiding negative figures error fixed
            'price': lambda x: random.randint(0, 300), 
            'beds': lambda x: random.randint(0, 5),
            'bedrooms': lambda x: random.randint(0, 5),
            'baths': lambda x: random.randint(0, 5),
            'guests': lambda x: random.randint(0, 5),
        })
        #9.4 Creating random room photos 
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            room = Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 13)):
                Photo.objects.create(caption=seeder.faker.sentence(), room=room, file=f'/media/{random.randint(1, 30)}.png')
            #9.5
            for amenity in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(amenity) # How to include elements in ManyToManyField
            for facility in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(facility) 
            for rule in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.rules.add(rule) 

        self.stdout.write(self.style.SUCCESS(f'{number} rooms created!'))