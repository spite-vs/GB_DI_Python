# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

MAX_WEIGHT = 100
back = {'спички': 1, 
        'палатка': 300, 
        'котелок': 50, 
        'компас': 3, 
        'кружка': 20, 
        'ложка': 10, 
        'дождевик': 40, 
        'спальный мешок': 100, 
        'тушенка': 100, 
        'вода': 400, 
        'алкоголь': 50, 
        'крупа': 100, 
        'нож': 10}


# #Единственный вариант с максимальным количесвом вещей в рюкзаке
# equipment = []
# cur_weight = 0
# back_sorted = dict(sorted(back.items(), key=lambda x: x[1]))

# for item, weight in back_sorted.items():
#     if cur_weight + weight <= MAX_WEIGHT:
#         equipment.append(item)
#         cur_weight += weight

# print('В рюкзак поместилось:\n',"\n".join(equipment), sep='')
# print(f'\nВес рюкзака: {cur_weight}')


#Все возможные варианты с заданным весом рюкзака
from itertools import combinations

combs = []
for i in range(len(back)):
    for var in combinations(back.items(), i):
        total_weight = sum(item[1] for item in var)
        if total_weight <= MAX_WEIGHT:
            combs.append((var, total_weight))

for i,comb in enumerate(combs):
    temp = {}
    for item in comb[0]:
        temp[item[0]] = item[1]
    if temp:
        print(f'{i}. {temp}, вес: {comb[1]}')