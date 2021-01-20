#Написать программу, которая вычисляет массу, плотность или объем,
#используя формулу m = Vρ. Пользователь выбирает, что он хочет
#вычислить и вводит два известных параметра.

def weight(v, ro):
    m = v * ro
    return m

def volume(m, ro):
    v = m / ro
    return v

def density_body(m, v):
    ro = m / v
    return ro

def calculations():
    print(' Если хотите вычислить массу, нажмите 1,\n если хотите вычислить объем, нажмите 2,\n если хотите вычислить плотность, нажмите 3')
    choice = input()
    choice = int(choice)
    return choice

def formula():
    a = calculations()
    if a == 1:
        v = input('Введите объем v: ')
        ro = input('Введите объем ro: ')
        v = float(v)
        ro = float(ro)
        return weight(v, ro)
    elif a == 2:
        m = input('Введите массу m: ')
        ro = input('Введите объем ro: ')
        m = float(m)
        ro = float(ro)
        return volume(m, ro)
    elif a == 3:
        m = input('Введите массу m: ')
        v = input('Введите объем v: ')
        m = float(m)
        v = float(v)
        return density_body(m, v)
    else:
        print('Введено неверное значение')

def runner():
    print(formula())

runner()
