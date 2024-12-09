from django.contrib import admin
from .models import Radar, ChannelMap, Point, RadarData

admin.site.register(Radar)
admin.site.register(ChannelMap)
admin.site.register(RadarData)
admin.site.register(Point)