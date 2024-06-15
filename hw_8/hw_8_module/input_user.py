import json
from pathlib import Path


__all__ = ['input_user']


def input_user(path: Path) -> None:
    """Создаёт json с введёнными через терминал параметрами пользователя"""
    unique_id = set()
    if not path.is_file():
        data = {level+1:{} for level in range(7)}
    else:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # unique_id = {id for id_name in data.values() for id in id_name.keys()}
            for id_name in data.values():
                unique_id.update(id_name.keys())
        
    while name := input('Введите имя пользователя: '):
        level = input('Введите уровень доступа от 1 до 7: ')
        user_id = input('Введите id пользователя: ')
        if user_id not in unique_id:
            unique_id.add(user_id)
            data[level].update({user_id: name})
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        else:
            print('Такой id пользователя уже существует')
            
            
if __name__ == '__main__':
    input_user(Path('users.json'))