from iotapp.models import Building, Room, DeviceType, Plan, Device, Data
from os import environ
import sys
from django.utils import timezone
import pandas as pd
pd.options.mode.chained_assignment = None
def dataroom(data,nameroom = 'room4_temperature'):
    df = data[(data['name'] == nameroom)]
    df.index = pd.to_datetime(df.time)
    df.drop('time', axis=1, inplace=True)
    df = df.resample('1min').ffill().dropna()
    return df
class ReadData:
    def __init__(self, minutes=30):
        self.minutes = minutes
    def read(self, name='temperature', no = 'cab'):
        now = timezone.now()
        #day = timezone.timedelta(days=self.days)
        minut = timezone.timedelta(minutes = self.minutes)
        delta = (now - minut)
        #print(now)
        #print(delta)
        #запрос
        data = Data.objects.filter(name__iendswith = name, createdAt__gte=delta).exclude(name__startswith = no).order_by('createdAt')
        #создаем датасет
        time_result = [entry.createdAt for entry in data]  # converts QuerySet into Python list
        name_result = [entry.name for entry in data]  # converts QuerySet into Python list
        value_result = [entry.value for entry in data]  # converts QuerySet into Python list
        df = pd.DataFrame({'time': time_result,
                           'value': value_result,
                           'name': name_result,})
        #приводим к одной шкале
        uniqrooms = pd.unique(df['name'])
        if len(uniqrooms) > 0:
            dataframe0 = dataroom(df,f'room1_{name}')
            dataframe1 = dataroom(df, f'room2_{name}')
            df01 = dataframe0.merge(dataframe1, left_on=dataframe0.index, right_on=dataframe1.index, how='left')
            x = dataframe0.index.strftime('%m-%d, %H:%M').to_list()
            y = dataframe0['value'].to_list()
            df01.index = pd.to_datetime(df01.key_0)
            Xall = df01.index.strftime('%m-%d, %H:%M').to_list()
            y0 = df01['value_x'].to_list()
            y1 = df01['value_y'].to_list()
            return Xall,[y0,y1]
        return [], [[]]
    def readmq(self, name='room4'):
        now = timezone.now()
        #day = timezone.timedelta(days=self.days)
        minut = timezone.timedelta(minutes = self.minutes)
        delta = (now - minut)
        #print(now)
        #print(delta)
        #запрос
        data = Data.objects.filter(name__contains = name, createdAt__gte=delta).order_by('createdAt')
        #создаем датасет
        time_result = [entry.createdAt for entry in data]  # converts QuerySet into Python list
        name_result = [entry.name for entry in data]  # converts QuerySet into Python list
        value_result = [entry.value for entry in data]  # converts QuerySet into Python list
        df = pd.DataFrame({'time': time_result,
                           'value': value_result,
                           'name': name_result,})
        #print(df)
        #приводим к одной шкале
        uniqrooms = pd.unique(df['name'])
        dataframe0 = dataroom(df, f'{name}2')
        mqnom = 5
        for item in uniqrooms:
            if item.find("mq4") != -1:
                mqnom = 4
        if len(uniqrooms) > 0:
            dataframe0 = dataroom(df, f'{name}2')
            dataframe1 = dataroom(df, f'{name}{mqnom}')
            df01 = dataframe0.merge(dataframe1, left_on=dataframe0.index, right_on=dataframe1.index, how='left')
            x = dataframe0.index.strftime('%m-%d, %H:%M').to_list()
            y = dataframe0['value'].to_list()
            df01.index = pd.to_datetime(df01.key_0)
            Xall = df01.index.strftime('%m-%d, %H:%M').to_list()
            y0 = df01['value_x'].to_list()
            y1 = df01['value_y'].to_list()
            return Xall,[y0,y1]
        return [], [[]]


