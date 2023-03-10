from django.shortcuts import render
#https://github.com/peopledoc/django-chartjs
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
#https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
# Create your views here.
from random import randint
from django.views import View
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView,BaseLineOptionsChartView
from chartjs.colors import next_color
from ReadDatafromBase import ReadData
class ChartMixin(object):
    def get_colors(self):
        #японские иероглифы цветов
        # 赤 / 緑 / 青　
        #https://qtatsu.hatenablog.com/?page=1600594307
        l = [(200, 0, 0), (0, 200, 0), (0, 0, 200)]
        return next_color(l)

    def get_providers(self):
        """Return names of datasets."""
        return ["temp", "sound", "Air"]
class lineChartJSONView(ChartMixin, BaseLineOptionsChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]
    def get_data(self):
        """Return 3 dataset to plot."""

        r = randint(30, 60)
        return [[r, 44, 92, 11, 44, 95, 35],
                [r, 92, 18, 3, 73, 87, 92],
                [r, 21, 94, 3, 90, 13, 65]]

    def get_options(self):
        options = {
            "title": {"display": True, "text": f"Room{self.kwargs['id']}"},
            "elements": {"point": {"pointStyle": "rectRounded", "radius": 4}},
            #"responsive": False,
            "animation": False,
            "roomid": self.kwargs['id'],
        }
        return options
#формируем Json для графика температуры
class TemperatureJSONView(BaseLineOptionsChartView):
    def get_colors(self):
        #японские иероглифы цветов
        # 赤 / 緑 / 青　
        #https://qtatsu.hatenablog.com/?page=1600594307
        l = [(0, 0, 200), (0, 200, 0)]
        return next_color(l)

    def get_providers(self):
        """Return names of datasets."""
        return ["№101", "№102"]
    def get_labels(self):
        """Return 7 labels."""
        #print(self.kwargs['id'])
        r = randint(30, 60)
        temp = ReadData()
        x, y = temp.read(name='temperature')
        #print(self.kwargs['id'])
        self.X_values = x
        self.Y_values = y
        return self.X_values
    def get_data(self):
        """Return 2 dataset to plot."""
        return self.Y_values

    def get_options(self):
        options = {
            "title": {"display": True, "text": f"Температура, С"},
            "elements": {"point": {"pointStyle": "rectRounded", "radius": 4}},
            #"responsive": False,
            "animation": False,
            "roomid": self.kwargs['id'],
        }
        return options
class HumJSONView(BaseLineOptionsChartView):
    def get_colors(self):
        #японские иероглифы цветов
        # 赤 / 緑 / 青　
        #https://qtatsu.hatenablog.com/?page=1600594307
        l = [(0, 0, 200), (0, 200, 0)]
        return next_color(l)

    def get_providers(self):
        """Return names of datasets."""
        return ["№101", "№102"]
    def get_labels(self):
        """Return 7 labels."""
        #print(self.kwargs['id'])
        r = randint(30, 60)
        temp = ReadData()
        x, y = temp.read(name='humidity')
        #print(self.kwargs['id'])
        self.X_values = x
        self.Y_values = y
        return self.X_values
    def get_data(self):
        """Return 2 dataset to plot."""
        return self.Y_values

    def get_options(self):
        options = {
            "title": {"display": True, "text": f"Влажность, %"},
            "elements": {"point": {"pointStyle": "rectRounded", "radius": 4}},
            #"responsive": False,
            "animation": False,
            "roomid": self.kwargs['id'],
        }
        return options
class MQJSONView(BaseLineOptionsChartView):
    def get_colors(self):
        #японские иероглифы цветов
        # 赤 / 緑 / 青　
        #https://qtatsu.hatenablog.com/?page=1600594307
        l = [(128, 128, 0), (0, 128, 128)]
        return next_color(l)

    def get_providers(self):
        """Return names of datasets."""
        return ["MQ2", "MQX"]
    def get_labels(self):
        """Return 7 labels."""
        #print(self.kwargs['id'])
        r = randint(30, 60)
        temp = ReadData()
        x, y = temp.readmq(name = f"room{self.kwargs['id']}_mq")
        self.X_values = x
        self.Y_values = y
        return self.X_values
    def get_data(self):
        """Return 2 dataset to plot."""
        return self.Y_values

    def get_options(self):
        options = {
            "title": {"display": True, "text": f"Датчики газа, ед."},
            "elements": {"point": {"pointStyle": "rectRounded", "radius": 4}},
            #"responsive": False,
            "animation": False,
            "roomid": self.kwargs['id'],
        }
        return options


line_chart = TemplateView.as_view(template_name='iotapp/line_chart.html')#line_chart
line_chart_json = lineChartJSONView.as_view()
main_view = TemplateView.as_view(template_name='iotapp/index.html')#line_chart
temp_chart = TemperatureJSONView.as_view()
hum_chart = HumJSONView.as_view()
mq_chart = MQJSONView.as_view()