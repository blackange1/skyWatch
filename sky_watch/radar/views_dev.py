import math
from time import sleep

from django.shortcuts import render
from django.http import JsonResponse

from radar.models import ChannelMap, Radar, RadarData
from .tools import Event, HEIGHT, WIDTH


#######################
# Block for Developer #
#######################

def radar_test_page(request):
    return render(request, "radar/radar_test.html")


def data_clear(request):
    """
    :param request:
    :return: json info about event of delete data in database
    """
    event_info = {}
    event_count = 0
    radars = Radar.objects.all()
    for radar in radars:
        event_count += 1
        event_info.update({f'event {event_count}': f'delete {radar.name}'})
        radar.delete()
    return JsonResponse(event_info)


def data_update(request):
    """
    :param request:
    :return: json info about event of update data in database
    """
    event = Event()

    # create Radar
    data_radars = [
        ("esp32-v1", "cnianb35pa8abwbi840bqaqo", True),
        ("esp32-v2", "opvcn8wosa3p4sdffe4ivm42", False),
    ]
    for name, secret_key, is_left in data_radars:
        try:
            Radar.objects.get(name=name)
        except BaseException as e:
            Radar.objects.create(
                name=name,
                secret_key=secret_key,
                is_left=is_left,
            )
            event.add(f'create radar {name}')

    # create channel_map__name == 'poltava'
    channel_map = ChannelMap.objects.filter(name="poltava")

    if not channel_map:
        ChannelMap.objects.create(
            name="poltava",
            radar_1=Radar.objects.get(name="esp32-v1"),
            radar_2=Radar.objects.get(name="esp32-v2"),
        )
        event.add(f"create channel_map__name == 'poltava'")

    radar_left = Radar.objects.get(name="esp32-v1")
    radar_right = Radar.objects.get(name="esp32-v2")
    # create RadarData, дивись гугл таблицю
    angle_left = [86, 77, 65, 52, 42, 32, 26, 21, 17, 14]
    angle_right = [148, 147, 145, 142, 146, 152, 154, 156, 160, 166]
    for i in range(min(len(angle_left), len(angle_right))):
        RadarData.objects.create(
            angle=angle_left[i],
            radar=radar_left,
        )
        RadarData.objects.create(
            angle=angle_right[i],
            radar=radar_right,
        )
        sleep(1)
        print('RadarData create', i + 1)
        event.add(f"create RadarData left and right")
    return JsonResponse(event.get_data())


def get_test_coordinate(request, angle_left, angle_right):
    """
    :test: get_test_coordinate(request, 45, 135) => {x: 600, y: 200} if WIDTH == 1200
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
    return JsonResponse({
        "x": x,
        #  HEIGHT - y оскільки початок координат в SVG знаходиться у лівому верхньому куті
        "y": HEIGHT - y,
    })
