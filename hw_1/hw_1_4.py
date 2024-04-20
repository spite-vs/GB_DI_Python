# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPS = 10

a = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(ATTEMPS):
    b = int(input(f'Отгадай число от {LOWER_LIMIT} до {UPPER_LIMIT} (осталось {ATTEMPS-i} попыток): '))
    if b > a:
        print('Загаданное число меньше')
    elif b < a:
        print('Загаданное число больше')
    else:
        print(f'Конгратулатинг! Вы отгадали загаданное число {a} за {i+1} попыток')
        break
else:
    print('Попытки закончились, приходите завтра')    
