# Написать программу, которая выполняет над двумя вещественными
# числами одну из четырех арифметических операций (сложение,
# вычитание, умножение или деление). Числа и операцию вводит
# пользователь.


def summ(a, b):
    summ_ = a + b
    return summ_


def minus(a, b):
    minus_ = a - b
    return minus_


def umnog(a, b):
    summ_ = a * b
    return summ_


def delit(a, b):
    summ_ = a / b
    return summ_


def doit(a, b, do):
    if do == '+':
        doit_ = summ(a, b)
    elif do == '-':
        doit_ = minus(a, b)
    elif do == '*':
        doit_ = umnog(a, b)
    elif do == '/':
        doit_ = delit(a, b)
    return doit_


def runner():
    total = doit(a, b, do)
    print(total)


a = float(input('a = '))
b = float(input('b = '))
do = input('введите знак: ')

runner()
