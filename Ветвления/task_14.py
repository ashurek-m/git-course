# По введенным длинам трех отрезков определить, можно ли из них
# составить треугольник при условии, что у треугольника сумма любых
# двух сторон должна быть не меньше третьей.

def info_treangle():
    a = float(input('Введите размер стороны a: '))
    b = float(input('Введите размер стороны b: '))
    c = float(input('Введите размер стороны c: '))
    list_treagle = [a, b, c]
    return list_treagle


def treagle(data):
    line1 = (data[0] + data[1]) > data[2]
    line2 = (data[1] + data[2]) > data[0]
    line3 = (data[2] + data[0]) > data[1]
    if (line1 and line2 and line3) == True:
        text = 'Из данных отрезков треугольник построить можно'
    else:
        text = 'Треугольник не пострроить'
    return text


def runner():
    print(treagle(info_treangle()))


runner()
