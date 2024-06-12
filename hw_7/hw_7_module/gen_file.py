from random import choices, randint
from string import ascii_lowercase, digits
from pathlib import Path
import os


__all__ = ['gen_file', 'get_different_files']


def gen_file(ext:str, min_name:int=6, max_name:int=30, min_size:int=256, 
             max_size:int=4096, file_count:int=42)->None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data = bytes(randint(0,255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)
        

def get_different_files(directory:str|Path, **kwargs)->None:
    """Генератор файлов с заданным расширением"""
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, num in kwargs.items():
        gen_file(ext, file_count=num)
        
if __name__ == '__main__':
    get_different_files(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_7\trash', bin=2, jpeg=2, mov=1, bmp=2, png=3, avi=3)