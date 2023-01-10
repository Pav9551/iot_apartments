from django.shortcuts import render
#https://github.com/peopledoc/django-chartjs

#https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
# Create your views here.
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartjs.colors import next_color
class ChartMixin(object):
    def get_colors(self):
        #японские иероглифы цветов
        # 赤 / 緑 / 青　
        #https://qtatsu.hatenablog.com/?page=1600594307
        l = [(200, 0, 0), (0, 200, 0), (0, 0, 200)]
        return next_color(l)

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]
class LineChartJSONView(ChartMixin,BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]
    def get_data(self):
        """Return 3 dataset to plot."""
        r = randint(30, 60)
        return [[r, 44, 92, 11, 44, 95, 35],
                [r, 92, 18, 3, 73, 87, 92],
                [r, 21, 94, 3, 90, 13, 65]]
class LineChartJSONView_Room1(ChartMixin,BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        
        X_labels = [1, 2, 3, 4, 5, 6, 7]
        r = randint(30, 60)
        self.Y_values = [[r, 44, 92, 11, 44, 95, 35],
                        [r, 92, 18, 3, 73, 87, 92],
                        [r, 21, 94, 3, 90, 13, 65]]
        return X_labels
    def get_data(self):
        """Return 3 dataset to plot."""
        return self.Y_values

line_chart = TemplateView.as_view(template_name='iotapp/line_chart.html')#line_chart
line_chart_json = LineChartJSONView_Room1.as_view()

def main_view(request):
    return render(request, 'iotapp/index.html')