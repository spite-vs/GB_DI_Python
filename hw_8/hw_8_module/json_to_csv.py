import json
import csv
from pathlib import Path 


__all__ = ['json_to_csv']


def json_to_csv(path: Path)->None:
    """Создаёт на основе json-файла одноимённый csv"""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    result = []
    for level, id_name in data.items():
        for id, name in id_name.items():
            result.append({'level':int(level), 'id': int(id), 'name': name})
    with open(path.stem + '.csv', 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.DictWriter(f, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(result)
        
        
if __name__ == '__main__':
    json_to_csv(Path('users.json'))