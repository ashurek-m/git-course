# В зависимости от того, что выберет пользователь, вычислить площадь
# либо прямоугольника (S = ab), либо треугольника (S=sqrt(p(p-a)(p-b)(p-c))),
# где p-полупериметр), либо круга (S=pi*r**2).
# Если выбраны прямоугольник или треугольник, то надо запросить длины
# сторон, если круг, то его радиус.

import math


def area_triangle(edge):
    half_meter = (edge[0] + edge[1] + edge[2]) / 2
    area = math.sqrt(half_meter * (half_meter - edge[0]) * (half_meter - edge[1]) * (half_meter - edge[2]))
    return area


def area_rectangle(edge):
    area = edge[0] * edge[1]
    return area


def area_circle(radius):
    area = math.pi * radius ** 2
    return area


def info_triangle():
    info_list = []
    a = float(input('Введите размер стороны a: '))
    info_list.append(a)
    b = float(input('Введите размер стороны b: '))
    info_list.append(b)
    c = float(input('Введите размер стороны c: '))
    info_list.append(c)
    return info_list


def info_rectangle():
    info_list = []
    a = float(input('Введите размер стороны a: '))
    b = float(input('Введите размер стороны b: '))
    info_list.append(a,b)
    return info_list


def info_circle():
    r = float(input('Введите размер радиуса r: '))
    return  r


def choice():
    choice_ = int(input('Нажмите 1 что бы вычислить площадь треугольника,\n'
                        'нажмите 2 что бы вычислить площадь прямоугольника,\n'
                        'нажмите 3 что бы вычичлить площадь окружности: '))
    if choice_ == 1:
        data = info_triangle()
        s = area_triangle(data)
    elif choice_ == 2:
        data = info_rectangle()
        s = area_rectangle(data)
    elif choice_ == 3:
        data = info_circle()
        s = area_circle(data)
    else:
        print('Введено неверное значение')
        s = choice()
    return s


print(choice())