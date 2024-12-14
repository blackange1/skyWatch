from django.urls import path
from . import views_dev, views_main

urlpatterns = [
    # prod
    path('', views_main.index, name='index'),
    path('radar/<str:channel>', views_main.radar, name='radar'),
    path('api/radar/<str:channel>', views_main.api_coordinate, name='api_coordinate'),
    # for developer
    path('dev/data/update', views_dev.data_update, name='dev_data_update'),
    path('dev/data/clear', views_dev.data_clear, name='dev_data_clear'),
    path('dev/radar', views_dev.radar_test_page, name='dev_radar_test_page'),
    path('dev/get-coordinate/<int:angle_left>/<int:angle_right>', views_dev.get_test_coordinate,
         name='dev_get_coordinate'),
]
