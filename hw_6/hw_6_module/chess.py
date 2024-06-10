
# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, 
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, 
# а если бьют - ложь.
# 4. Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint

__all__ = ['generate_squares', 'is_hit']

def is_hit(squares):
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            if squares[i][0] == squares[j][0] or squares[i][1] == squares[j][1] or abs(squares[i][0] - squares[j][0]) == abs(squares[i][1] - squares[j][1]):
                return False
    return True


def generate_squares():
    squares = []
    while len(squares) < 8:
        new_square = (randint(1, 8), randint(1, 8))
        if new_square not in squares:
            squares.append(new_square)
    return squares


if __name__ == "__main__":
    true_values = [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]
    x = generate_squares()
    print(x,is_hit(x), sep='\n')
    print(is_hit(true_values))
    
