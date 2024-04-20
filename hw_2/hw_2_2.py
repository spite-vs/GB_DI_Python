# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

DICT_HEX = '0123456789abcdef'

original_num = int(input('Введите число: '))

hex_num = ''
if original_num == 0:
    hex_num = '0'
num = abs(original_num)
while num:
    index = num%16
    hex_num = DICT_HEX[index] + hex_num
    num //=16

sign = '-' if original_num < 0 else ''
print(f'Число {original_num} в шеснадцатеричном формате: {sign}0x{hex_num}')
print(f'Контроль: {hex(original_num)}')