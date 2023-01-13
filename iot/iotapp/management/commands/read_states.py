from django.core.management.base import BaseCommand
from ReadDatafromBase import ReadData
class Command(BaseCommand):
    def handle(self, *args, **options):
        temp = ReadData(2)
        x, y = temp.read(name='temperature')
        print(x)
        print(y)












