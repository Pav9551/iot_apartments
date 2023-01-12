from iotapp.models import Building, Room, DeviceType, Plan, Device, Data
from os import environ
import sys
from django.utils import timezone
import pandas as pd


class ReadData:
    def __init__(self, days):
        self.days = 1
    def read(self, name='room4_temperature', no = 'cab'):
        now = timezone.now()
        day = timezone.timedelta(days=self.days)
        min5 = timezone.timedelta(minutes=2)
        delta = (now - day)
        print(now)
        print(delta)
        # self.value, self.name, self.createdAt
        data = Data.objects.filter(name__iendswith = name, createdAt__gte=delta).exclude(name__startswith = no).order_by('createdAt')
        print(data)
        time_result = [entry.createdAt for entry in data]  # converts QuerySet into Python list
        value_result = [entry.value for entry in data]  # converts QuerySet into Python list
        df = pd.DataFrame({'time': time_result,
                           'value': value_result})
        df.index = pd.to_datetime(df.time)
        df.drop('time', axis=1, inplace=True)
        df = df.resample('10min').ffill().dropna()
        x = df.index.strftime('%m-%d, %H:%M').to_list()

        y = df['value'].to_list()
        return x,[y]

