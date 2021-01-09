import math

a = input('Введите длину катета a: ')
b = input('Введите длину катета b: ')

a2 = int(a)
b2 = int(b)

def hypotenuse(katet_1, katet_2):
    c = math.sqrt(katet_1 ** 2 + katet_2 ** 2)
    return c

def perimeter_of_the_triangle(a, b, c):
    p = a + b + c
    return p

def area_of_the_triangle(a, b):
    s = 1 / 2 * (a * b)
    return s

def runner():
    perimeter = perimeter_of_the_triangle(a2, b2, hypotenuse(a2, b2))
    area = area_of_the_triangle(a2, b2)
    print('Периметр треугольника: {:.2f}'.format(perimeter))
    print('Площадь треугольника: {:.2f}'.format(area))

runner()
