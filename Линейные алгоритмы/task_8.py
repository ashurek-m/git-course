#Напишите программу, которая вычисляет площадь поверхности цилиндра
#по заданным с клавиатуры радиусу и высоте цилиндра. Формула площади
#одного основания цилиндра: S = πr2. Формула площади боковой
#поверхности цилиндра: S = 2πrh.
import math

specified_radius = input('Введите радиус цилиндра: ')
specified_height = input('Введите высоту цилиндра: ')

specified_radius = float(specified_radius)
specified_height = float(specified_height)

def area(r):
    s_area = math.pi * r ** 2
    return s_area

def forming_part(r, h):
    s_part = 2 * math.pi * r * h
    return s_part

def area_cylinder(r, h):
    s_cylinder = 2 * area(r) + forming_part(r, h)
    return s_cylinder

def runner():
    cylinder = area_cylinder(specified_radius, specified_height)
    print('Площадь цилиндра равна: {:.2f}'.format(cylinder))

runner()
