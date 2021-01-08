liter = input('Введите номер буквы: ')
liter  = int(liter)

def numder_liter(numder):
    first_liter = ord('a')
    number_search = first_liter + numder - 1
    liter_search = chr(number_search)
    print(f'Искомая буква: {liter_search}')

def runner():
    numder_liter(liter)

runner()
