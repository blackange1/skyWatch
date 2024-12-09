import math
from time import sleep

from django.shortcuts import render
from django.http import JsonResponse

from radar.models import ChannelMap, Radar, RadarData
from .tools import Event, HEIGHT, WIDTH


def get_coordinate(angle_left, angle_right):
    """
    :test: get_coordinate(45, 135) => {x: 600, y: 200} if WIDTH == 1200
    :param request: angle_left: кут лівого esp32, angle_right: кут правого esp32
    :return: get x and y coordinates
    """
    # знаходимо k-коефіцієнт рівнянн y = k * x + c
    k1 = math.tan(math.pi / 180 * angle_left)
    k2 = math.tan(math.pi / 180 * angle_right)
    # знаходимо c2 рівняня y = k2 * x + c2
    # враховуючи, що пряма проходить через точеку (0, WIDTH)
    c2 = -k2 * WIDTH
    # розв'я зуємо систему рівнянь y = k1 * x та y = k2 * x + c2 шляхлм підстановки
    x = c2 / (k1 - k2)
    y = k1 * x
    return {
        "x": x,
        #  HEIGHT - y оскільки початок координат в SVG знаходиться у лівому верхньому куті
        "y": HEIGHT - y,
    }


def api_coordinate(request, channel):
    """
    :param request: channel is name of object ChannelMap
    :return: get [{x: 600, y: 600}...]
    """
    channel_map = ChannelMap.objects.get(name=channel)
    radar_1 = channel_map.radar_1
    radar_2 = channel_map.radar_2
    data_1 = radar_1.radardata_set.all().order_by('created_date')[:10]
    data_2 = radar_2.radardata_set.all().order_by('created_date')[:10]
    if len(data_1) != len(data_2):
        return JsonResponse({
            "status": f"problem esp32: count data {len(data_1)} != {len(data_2)}",
        })
    coordinates = []
    for i in range(len(data_1)):
        coordinates.append(
            get_coordinate(
                data_1[i].angle,
                data_2[i].angle
            )
        )
        print(data_1[i], data_2[i])
    return JsonResponse({
        "status": "ok",
        "coordinates": coordinates,
    })


def radar(request, channel):
    name_space = ""
    channel_map = ChannelMap.objects.filter(name=channel)

    if channel_map:
        channel_map = channel_map[0]
        name_space = channel_map.name
    else:
        return render(request, "radar/radar.html", {
            "name_space": name_space,
            "channel": channel,
        })
    context = {
        "channel": channel,
        "name_space": name_space,
    }
    return render(request, "radar/radar.html", context=context)
