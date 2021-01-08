apple = input('Количество яблок: ')
children = input('Количество школьников: ')

apple = int(apple)
children = int(children)

def apple_result(apple, children):
    #количество яблок которые достануться школьника
    apple_sh = apple // children
    #количество яблок которое останется в корзине
    apple_box = apple % children
    print(f' По {apple_sh} яблок достанется каждому ученика.\n', f'В корзине останется {apple_box} яблок')

def runner():
    apple_result(apple, children)


runner()
