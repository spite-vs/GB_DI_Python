from pathlib import Path
from hw_8_module.csv_to_json import *
from hw_8_module.csv_to_pickle import *
from hw_8_module.input_user import *
from hw_8_module.json_to_csv import *
from hw_8_module.json_to_pickle import *
from hw_8_module.pickle_to_csv import *
from hw_8_module.walk_saver import *
from hw_8_module.write_json import *


# write_json(Path(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_7\result.txt'))
# input_user(Path('users.json'))
# json_to_csv(Path('users.json'))
# csv_to_json(Path('users.csv'), Path('new_users.json'))
# json_to_pickle(Path(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_8'))
# csv_to_pickle(Path('new_users.csv'))
# pickle_to_csv(Path('new_users.pickle'))

walk_saver(Path(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_8'))
