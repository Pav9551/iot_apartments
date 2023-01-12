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
        print(self.kwargs['id'])
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
        return ["Room1", "Room2"]
    def get_labels(self):
        """Return 7 labels."""
        print(self.kwargs['id'])
        r = randint(30, 60)

        '''def load_goods_from_base(self):
            goods = Good.objects.all()
            list_result = [entry.name for entry in goods]  # converts QuerySet into Python list
            data = {'name': list_result}
            self.excel_data_df = pd.DataFrame(data, columns=['name'])
            print(self.excel_data_df)'''

        self.X_values = [1, 2, 3, 4, 5, 6, 7]
        self.Y_values = [[r, 44, 92, 11, 44, 95, 35],
                         [r, 92, 18, 3, 73, 87, 92]]
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



line_chart = TemplateView.as_view(template_name='iotapp/line_chart.html')#line_chart
line_chart_json = lineChartJSONView.as_view()
main_view = TemplateView.as_view(template_name='iotapp/index.html')#line_chart
temp_chart = TemperatureJSONView.as_view()
