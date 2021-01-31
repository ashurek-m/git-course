# Определить, принадлежит ли точка с координатами (x; y) кругу радиуса R
# с центром в начале координат. Пользователь вводит координаты точки и
# радиус круга.

import math


def info_task():
    info_ = {}
    info_['x'] = float(input('x = '))
    info_['y'] = float(input('y = '))
    info_['r'] = float(input('r = '))
    return info_


def proverka(data):
    g = math.sqrt(data['x'] ** 2 + data['y'] ** 2)
    if g <= data['r']:
        text = 'x and y in r'
    else:
        text = 'x and y not in r'
    return text


def runner():
    print(proverka(info_task()))


runner()