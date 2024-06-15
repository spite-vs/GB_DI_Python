import json
import csv
from pathlib import Path


__all__ = ['csv_to_json']


def csv_to_json(from_path: Path, to_path: Path) -> None:
    """Создаёт на основе указанного csv-файла json с указанием нового имени для него"""
    result = []
    with open(from_path, 'r', encoding='utf-8', newline='') as f:
        csv_read = csv.reader(f, dialect='excel-tab')
        for i, item in enumerate(csv_read):
            if i != 0:
                level, id, name = item
                data = {
                    'level': int(level),
                    'id': id.zfill(10),
                    # 'id': f'{int(id):010}',
                    'name': name.title(),
                    'hash': hash(f'{name.title()}{id.zfill(10)}')
                }
                result.append(data)
    with open(to_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
        
        
        
if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_users.json'))