# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


a = r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_5\hw_5_2.py'

def split_path(file: str)->tuple[str]:
    """Функция разделения пути к файлу, названия файла и его расширения"""
    path = '\\'.join(file.split('\\')[:-1])
    name, extension = file.split('\\')[-1].split('.')
    return path, name, extension


print(split_path(a))