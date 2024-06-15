import json
import pickle
from pathlib import Path


__all__ = ['json_to_pickle']


def json_to_pickle(path: Path)->None:
    """Создаёт на основе всех json-файлов, лежащих в указанной директории одноимённые файлы формата pickle"""
    for obj in path.iterdir():
        if obj.is_file() and obj.suffix == '.json':
            with(
                open(obj, 'r', encoding='utf-8') as f_read,
                open(obj.stem + '.pickle', 'wb') as f_write
            ):
                data = json.load(f_read)
                pickle.dump(data, f_write)
                
                
                
if __name__ == '__main__':
    json_to_pickle(Path(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_8'))