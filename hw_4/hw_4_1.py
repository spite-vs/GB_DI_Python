# 1. Напишите функцию для транспонирования матрицы

from random import randint

def get_matrix()->list[list[int|float]]:
    """Фукция создания матрицы со случайной шириной и высотой от 1 до 10 и значениями от 1 до 100"""
    i = randint(1,10)
    j = randint(1,10)
    lst=[]
    for _ in range(i):
        row = []
        for _ in range(j):
            row.append(randint(1,100))
        lst.append(row)
    return lst
    
def matrix_trans(lst: list[list[int|float]])->list[list[int|float]]:
    """Фукция транспонирования матрицы"""
    return list(zip(*lst))

def print_matrix(lst: list[list[int|float]]):
    """Фукция печати матрицы"""
    for i in lst:
        for j in i:
            print(f'{j:<4}', end='')
        print()
    print()  
   
   
a=get_matrix()
print_matrix(a)
print_matrix(matrix_trans(a))