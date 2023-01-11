from django.urls import path
from iotapp import views
app_name = 'iotapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('charts', views.charts_view, name='charts'),
    path('tables', views.tables_view, name='tables'),
    path('chart', views.line_chart, name='line_chart'),
    path('chartJSON/<int:id>/', views.line_chart_json, name='line_chart_json'),
]
