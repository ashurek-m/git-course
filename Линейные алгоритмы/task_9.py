#Напишите программу, которая выводит уравнение прямой y = kx + b,
#проходящей через заданные точки. Координаты точек вводятся с
#клавиатуры.
print('Координаты первой точки х1 и у1:')
x1 = float(input('\tx1 = '))
y1 = float(input('\ty1 = '))
print('Координаты второй точки х2 и у2:')
x2 = float(input('\tx2 = '))
y2 = float(input('\ty2 = '))

def equation_straight_line(x1, x2, y1, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print('Уравнение прямой имеет вид: у = %.2f * x + %.2f'%(k, b))

equation_straight_line(x1, x2, y1, y2)
