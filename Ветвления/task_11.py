#Дана следующая функция y = f(x):
#y = x - 0.5, при x > 0;
#y = 0, при x = 0;
#y = |x|, при x < 0.
#Написать программу, определяющую значение y по переданному
#значению x.

x = input('Введите х: ')
x = float(x)

def function_y(x):
    if x > 0:
        y= x -0.5
    elif x < 0:
        y = abs(x)
    elif x == 0:
        y = x
    return y

def runner():
     print(function_y(x))

runner()
