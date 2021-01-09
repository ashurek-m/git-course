#По введенному с клавиатуры радиусу вычислить длину соответствующей
#окружности и площадь круга. Формулы: L = 2πr, S = πr2.
import math

radius = input('Введите радиус окружности: ')
radius = float(radius)

def circumference(r):
    l = 2 * math.pi * r
    return l

def area(r):
    s = math.pi * r ** 2
    return s

def runner():
    length = circumference(radius)
    area_circle = area(radius)
    print(f' Длина окружности равна: {length}\n',
          f'Площадь окружности равна:{area_circle}'
          )

runner()
