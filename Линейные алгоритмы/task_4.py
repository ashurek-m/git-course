#С клавиатуры вводятся границы числового диапазона. Получите
#случайное целое число в его пределах и выведите его на экран.
from random import randint

upper_limit = input('Нижняя граница: ')
lower_limit = input('Вепхняя граница: ')

upper_limit = int(upper_limit)
lower_limit = int(lower_limit)

def random_number(numder_1, numder_2):
    numder = randint(numder_1, numder_2)
    return numder

def runner():
    print(random_number(upper_limit, lower_limit))

runner()
