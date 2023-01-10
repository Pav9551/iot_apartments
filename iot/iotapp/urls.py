from django.urls import path
from iotapp import views
app_name = 'iotapp'

urlpatterns = [
    path('', views.line_chart, name='index'),
    path('chart', views.line_chart, name='line_chart'),
    path('chartJSON', views.line_chart_json, name='line_chart_json'),

]
