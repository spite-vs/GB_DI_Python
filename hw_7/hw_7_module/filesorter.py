from pathlib import Path
import os

__all__ = ['sort_files']
def sort_files(path:str|Path, groups:dict[str:list[str]]=None)->None:
    """Сортирует заданные форматы файлов по папкам"""
    if isinstance(path, str):
        path = Path(path)
    if not groups:
        groups = {
            Path('video'): ['avi', 'mov', 'mk4', 'mkv'],
            Path('images'): ['jpg', 'jpeg', 'bmp', 'png']
            }
    os.chdir(path)
    revers_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for ext in ext_list:
            revers_groups[f'.{ext}'] = target_dir
    for file in path.iterdir():
        if file.is_file() and file.suffix in revers_groups:
            file.replace(revers_groups[file.suffix] / file.name)
                


if __name__ == '__main__':
    sort_files(Path(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_7\sem_6'))