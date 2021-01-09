#Написать программу, которая генерирует случайное трехзначное число и
#вычисляет сумму его цифр.
from random import randint

MIN_NUMBER = 100
MAX_NUMBER = 999

def random_number(number_1, number_2):
    number = randint(number_1, number_2)
    return number

def sum_random(list):
    int_list = []
    result = 0
    for i in range(len(list)):
        row = int(list[i])
        result += row
    return result

def runner():
    iteration = str(random_number(MIN_NUMBER, MAX_NUMBER))
    list_number = list(iteration)
    print(list_number)
    fin = sum_random(list_number)
    print(fin)

runner()
