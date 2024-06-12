# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path
import os


__all__ = ['group_rename']

    
def group_rename(path:str|Path, new_file_name:str, ext_old:str, num_size: int=3, ext_new:str=None, range_char:tuple[int]=None)->None:
    """Групповое переименовывание файлов"""
    if isinstance(path, str):
        path = Path(path)
    os.chdir(path)
    number = 1
    number_limit = 10**num_size
    for file in path.iterdir():
        if file.is_file() and file.suffix == f'.{ext_old}':
            origin_char = file.name[(range_char[0]-1):range_char[1]] if range_char else ''
            new_name = f'{origin_char}{new_file_name}{str(number).zfill(num_size)}.{ext_new if ext_new else ext_old}'
            if Path(new_name).is_file():
                while number < number_limit:
                    new_name = f'{origin_char}{new_file_name}{str(number).zfill(num_size)}.{ext_new if ext_new else ext_old}'
                    if not Path(new_name).is_file():
                        Path(file).rename(new_name)
                    number +=1
            else:
                Path(file).rename(new_name)
            number +=1
            if number >= number_limit:
                number = 1
                



if __name__ == '__main__':
    group_rename(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_7\sem_6', 'Давай-давай', 'avi', 3,)