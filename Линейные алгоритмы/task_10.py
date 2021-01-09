#С клавиатуры вводятся два двоичных числа. Требуется вывести на экран в
#двоичном виде результаты побитовых операций И (plustilino)&), ИЛИ (plustilino)|),
#ИСКЛЮЧАЮЩЕЕ ИЛИ (plustilino)^) над этими числами.
n1 = input('n1 = ')
n2 = input('n2 = ')

n1 = int(n1,2)
n2 = int(n2,2)

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

print('Результат побитового OR: %10s' % bin(bit_or))
print('Результат побитового AND: %10s' % bin(bit_and))
print('Результат побитового XOR: %10s' % bin(bit_xor))
