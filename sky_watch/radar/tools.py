import math


class Event(object):
    def __init__(self):
        self.count = 0
        self.data = {}

    def add(self, msg):
        self.count += 1
        self.data.update({f'event {self.count}': msg})

    def get_data(self):
        if self.count:
            return self.data
        return {"message": "The required data was already in the database"}


WIDTH = 1200
HEIGHT = 800


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
