
from random import shuffle

__all__ = ['generate_squares']

def is_hit(squares):
    for i in range(8):
        for j in range(i+1, 8):
            if squares[i] == squares[j] or squares[i] - i == squares[j] - j or squares[i] + i == squares[j] + j:
                return False
    return True


def generate_squares():
    squares = list(range(1, 9))
    for i in range(4):
        shuffle(squares)
        while not is_hit(squares):
            shuffle(squares)
        print(squares)