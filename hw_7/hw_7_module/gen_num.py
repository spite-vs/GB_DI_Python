from random import randint, uniform
from pathlib import Path

__all__ = ['write_file']

MIN_NUM = -1000
MAX_NUM = 1000

def write_file(num_str: int, f_name:str | Path) -> None:
    """Генератор чисел"""
    with open(f_name, 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            print(f'{randint(MIN_NUM,MAX_NUM)} | {uniform(MIN_NUM,MAX_NUM)}', file=f)
            
if __name__ == '__main__':
    write_file(10, 'sem_1.txt')