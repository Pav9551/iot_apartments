from django.shortcuts import render
#https://github.com/peopledoc/django-chartjs
# Create your views here.
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartjs.colors import next_color

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_colors(self):
        # 赤 / 緑 / 青　
        #https://qtatsu.hatenablog.com/?page=1600594307
        l = [(200, 0, 0), (0, 200, 0), (0, 0, 200)]
        return next_color(l)
    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]


    def get_data(self):
        """Return 3 dataset to plot."""
        r = randint(30, 60)
        return [[r, 44, 92, 11, 44, 95, 35],
                [r, 92, 18, 3, 73, 87, 92],
                [r, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='iotapp/line_chart.html')#line_chart
line_chart_json = LineChartJSONView.as_view()


def main_view(request):
    return render(request, 'iotapp/index.html')