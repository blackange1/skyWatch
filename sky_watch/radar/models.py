from django.utils import timezone

from django.db import models


class Radar(models.Model):
    name = models.CharField(max_length=255, unique=True)
    secret_key = models.CharField(max_length=255)
    is_left = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RadarData(models.Model):
    angle = models.IntegerField()
    radar = models.ForeignKey(to=Radar, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    # TODO add geo_x and geo_y. If esp32 move
    # geo_x = models.FloatField()
    # geo_y = models.FloatField()

    def __str__(self):
        return f"{self.created_date} | {self.radar} | angle={self.angle}"


class ChannelMap(models.Model):
    name = models.CharField(max_length=255, unique=True)
    radar_1 = models.ForeignKey(to=Radar, related_name='r1_channel_map_set', on_delete=models.CASCADE)
    radar_2 = models.ForeignKey(to=Radar, related_name='r2_channel_map_set', on_delete=models.CASCADE)

    # TODO: If we wont show height target
    # radar_3 = models.ForeignKey(to=Radar, related_name='r3_channel_map_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    channel_map = models.ForeignKey(to=ChannelMap, on_delete=models.CASCADE)
