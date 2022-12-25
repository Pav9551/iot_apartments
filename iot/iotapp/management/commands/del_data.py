from django.core.management.base import BaseCommand
from iotapp.models import  Data

class Command(BaseCommand):
    def handle(self, *args, **options):
        Data.objects.all().delete()