# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её 
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
from pathlib import Path


__all__ = ['walk_saver']


def get_size(path):
    """Рекурсивно обходит текущую папку и суммирует размер файлов, расположенных в ней"""
    if path.is_file():
        return path.stat().st_size
    else:
        return sum(get_size(f) for f in path.iterdir())
    
    
def walk_saver(path: Path)->None:
    """Обходит все каталоги, начиная с текущего и создаёт json-файл с описанием параметров всех объектов в нём"""
    result = []
    for item in iter(path.rglob('*')):
        result.append({'name': item.name, 'parent': str(item.parent), 'type': 'file' if item.is_file() else 'dir', 'size': get_size(item)})
    
    with open(path.stem + '_stat.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    with open(path.stem + '_stat.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(result[0].keys()), dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(result)

    with open(path.stem + '_stat.pickle', 'wb') as f:
        pickle.dump(result, f)



if __name__ == '__main__':
    walk_saver(Path(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_8'))
