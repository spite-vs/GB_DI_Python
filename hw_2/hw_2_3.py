# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

frac_1 = input('Введите дробь в формате ?/?: ')
frac_2 = input('Введите дробь в формате ?/?: ')

num_1, denom_1 = map(int, frac_1.split('/'))
num_2, denom_2 = map(int, frac_2.split('/'))

num_sum_frac = num_1 * denom_2 + num_2 * denom_1
denom_sum_frac = denom_1 * denom_2

a = num_sum_frac
b = denom_sum_frac
while b:
    a, b = b, a % b
num_sum_frac //= a
denom_sum_frac //= a
print(a)
num_mul_frac = num_1 * num_2
denom_mul_frac = denom_1 * denom_2

a = num_mul_frac
b = denom_mul_frac
while b:
    a, b = b, a % b
num_mul_frac //= a
denom_mul_frac //= a
print(a)

print(f'Сумма дробей {frac_1} и {frac_2} равна {str(num_sum_frac)}/{denom_sum_frac}')
print(f'Произведение дробей {frac_1} и {frac_2} равно {num_mul_frac}/{denom_mul_frac}')


#Контроль

from fractions import Fraction

f_1 = Fraction(frac_1)
f_2 = Fraction(frac_2)
print(f'Сумма: {f_1+f_2}\nПроизведение: {f_1*f_2}')