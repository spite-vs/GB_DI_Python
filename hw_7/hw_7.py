from hw_7_module.gen_num import * 
from hw_7_module.gen_name import *
from hw_7_module.filemerging import *
from hw_7_module.gen_file import *
from hw_7_module.filesorter import *
from hw_7_module.renamer import *


write_file(12, 'numbers.txt')
gen_name(5,'names.txt')
sum_files('names.txt', 'numbers.txt','result.txt')
get_different_files(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_7\trash', bin=5, jpeg=7, mov=15, bmp=2, png=3, avi=12, doc=12, xls=3)
sort_files(r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_7\trash')
group_rename(path=r'C:\Users\spite\Downloads\Studies\GB\Data_Ingineer\Python\hw_7\trash', new_file_name='_Документ', ext_old='doc',num_size=4, ext_new='docx',range_char=(2,3))


