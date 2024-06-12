from pathlib import Path
from typing import TextIO

__all__ = ['sum_files']

def read_or_begin(fd:TextIO)->str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip()

def sum_files(f1_name:str|Path, f2_name:str|Path, res_f: str|Path) -> None:
    """Конкатенация файлов по условию"""
    with open(f1_name, encoding='utf-8') as f1, \
    open(f2_name, encoding='utf-8') as f2, \
    open(res_f, 'a', encoding='utf-8') as res:
        # len1 = sum(1 for _ in f1)
        # len2 = sum(1 for _ in f2)
        max_len = max(len(list(f1)),len(list(f2)))
        for _ in range(max_len):
            name = read_or_begin(f1)
            num_int, num_float = read_or_begin(f2).split(' | ')
            mult = int(num_int)*float(num_float)
            res.write(f'{name.lower()} {-mult}\n') if mult < 0 \
                else res.write(f'{name.upper()} {int(mult)}\n') if mult > 0 \
                else 42
        
        

if __name__ == '__main__':
    sum_files(Path('sem_2.txt'), Path('sem_1.txt'),Path('sem_3.txt'))   
