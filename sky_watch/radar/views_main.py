import json

from django.shortcuts import render
from django.http import JsonResponse

from radar.models import ChannelMap, RadarData, Radar
from .tools import get_coordinate


def index(request):
    list_channel_map = ChannelMap.objects.all()
    print(list_channel_map)
    context = {
        'list_channel_map': list_channel_map,
    }
    return render(request, 'radar/index.html', context=context)


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


def api_radar_data(request):
    if request.method == "POST":
        body = request.body
        data = json.loads(body.decode())
        radar_name = data.get("radar", "")
        radar = Radar.objects.filter(name=radar_name).first()
        if radar:
            angle = data.get("angle", None)
            if angle is None:
                return JsonResponse({
                    "status": "ok",
                    "error": "Не вкахано кут"
                })
            RadarData.objects.create(
                angle=angle,
                radar=radar,
            )
            return JsonResponse({
                "status": "ok",
            })
        return JsonResponse({
            "status": "ok",
            "error": "ESP-32 з таким іменем не існує"
        })
    return JsonResponse({
        "status": "ok",
        "info": "для перередачі даних використовуй метод POST, а інформацію передавай у body",
        "exemple body": {
            "angle": 45,
            "radar": "esp32-v1"
        }
    })
