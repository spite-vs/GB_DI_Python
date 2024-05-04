# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def hashable(x)->bool:
    """Функция проверки объекта на хэшируемость"""
    try:
        hash(x)
        return True
    except:
        return False
    
def new_dict(**kwargs)->dict:
    """Функция создания словаря через ключевые параметры, где значение становится ключом, а имя аргумента - значением"""
    res = {}
    for key, value in kwargs.items():
        if not hashable(value):
            value = str(value)
        res[value] = key
    return res


print(new_dict(x=[1,1], y=(1,2,3), z={1,2,3}, i={1:"qwe"}, j="qwe", k=1.25))