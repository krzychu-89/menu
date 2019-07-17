from django.core.management.base import BaseCommand, CommandError
from emenu.models import *
import random
from datetime import timedelta

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(15):
            o = Menu()
            o.name = f"Menu_{i}"
            o.description = f"Jakis tekst opisujący menu nr {i}"
            o.save()

        menus_ids = Menu.objects.all().values_list('id', flat=True)
        for i in range(150):
            o = Dish()
            o.name = f"Danie {i}"
            o.description =  f"Jakis tekst opisujący danie nr {i}"
            td = timedelta(hours=0, minutes=random.choice([10,15,20,25]))
            o.preparation_time = td
            o.is_vegetarian = random.choice([True, False])
            menu_obj = Menu.objects.get(id=random.choice(menus_ids))
            o.menu_id = menu_obj
            o.save()

        # menu bez dishes
        for i in range(15, 30):
            o = Menu()
            o.name = f"Menu_{i}"
            o.description = f"Jakis tekst opisujący menu nr {i}"
            o.save()


